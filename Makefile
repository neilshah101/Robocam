.PHONY: db-migrate db-seed db-psql

db-migrate:
	cp -n .env.example .env || true
	cp -n packages/db/.env.example packages/db/.env || true
	cd packages/db && alembic upgrade head

db-seed:
	cp -n .env.example .env || true
	cp -n packages/db/.env.example packages/db/.env || true
	cd packages/db && python seed.py

db-psql:
	cp -n .env.example .env || true
	docker compose --env-file .env -f infra/docker/docker-compose.yml exec postgres \
		psql -h localhost -U robocam -d robocam
