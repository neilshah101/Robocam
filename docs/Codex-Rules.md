# Codex Rules

You are coding in a production-grade, audit-safe style. Make the smallest possible changes, avoid
refactors, and never rewrite working code. Keep main stable, prefer feature branches, and commit in
small labeled units. Design APIs curl-first with clear examples, validate inputs, and scope all data.
Do not silently drop rows. Never commit __pycache__/, .pyc, build artifacts, or temp files.

## 1) No surprise rewrites
- Never refactor large areas for cleanliness.
- Make the smallest possible change that solves the problem.
- If a refactor is required, do it as a separate commit or PR with clear scope.

## 2) Work in thin slices
- Implement features in small vertical slices (DB -> API -> UI), one slice at a time.
- Each slice must be testable and shippable.

## 3) Always preserve existing behavior
- Default rule: do not break anything already working.
- If behavior must change, document it clearly in the PR description and commit message.

## 4) Audit-safety is non-negotiable
- Avoid silent data mutation.
- Capture before -> after state in an audit event or log table when relevant.
- Destructive changes must be explicitly user-triggered.

## 5) Error handling rules
- Do not throw raw tracebacks to users.
- Use proper HTTP status codes:
  - 401 auth
  - 403 permission
  - 404 missing
  - 400 validation
  - 409 conflict

## 6) Incremental and labeled commits
- Commit frequently, each commit equals one coherent change.
- Commit messages must be descriptive (module + feature + intent).
- Never commit junk: __pycache__/, .pyc, build artifacts, temp files.

## 7) Branch discipline (recommended workflow)
- Always create a branch per feature or fix: feature/<name> or fix/<name>.
- Merge only after tests pass, curl verification done, and UI verified locally.
- Keep main stable.

## 8) Production-grade code standards
- No quick hacks that skip validation or error handling.
- Validate inputs at the boundary (API layer).
- Use DB constraints where appropriate (or clearly planned later).
- Prefer clear code over clever code.

## 9) Do Not Do list
- Never do these without asking:
  - Changing folder structure
  - Renaming files broadly
  - Reformatting the whole repo
  - Converting styles or frameworks
  - Mass refactors
  - Upgrading everything

## 10) Do not invent paths or files
- Only modify files that exist.
- If a path is unknown, search in the repo or ask.

## 11) No fake fixes
- If unsure, show the exact error reasoning.
- Propose a minimal change.
- Include how to verify via curl or UI.

## 12) Output format (every response)
Always answer in this structure:
- What changed (1-3 bullets)
- Exact files touched
- Patch or code
- How to run
- How to verify
- curl commands for backend
- UI steps for frontend
- Git commands (add/commit/push)
