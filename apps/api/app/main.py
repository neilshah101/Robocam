from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import auth, schemas
from .db import get_db

from models import User

app = FastAPI(title="Robocam API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/auth/signup", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: schemas.SignupRequest, db: Session = Depends(get_db)) -> schemas.UserResponse:
    existing = db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already in use")

    user = User(email=payload.email, hashed_password=auth.hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return schemas.UserResponse(id=str(user.id), email=user.email)


@app.post("/auth/login", response_model=schemas.TokenResponse)
def login(payload: schemas.LoginRequest, db: Session = Depends(get_db)) -> schemas.TokenResponse:
    user = db.scalar(select(User).where(User.email == payload.email))
    if not user or not auth.verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = auth.create_access_token(str(user.id))
    return schemas.TokenResponse(access_token=token)


@app.get("/auth/me", response_model=schemas.UserResponse)
def me(current_user: User = Depends(auth.get_current_user)) -> schemas.UserResponse:
    return schemas.UserResponse(id=str(current_user.id), email=current_user.email)
