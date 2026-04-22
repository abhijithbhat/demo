# Soc Ops Workspace Guidelines

## Mandatory Checklist
Before concluding tasks, always verify:
- [ ] **Lint**: `uv run ruff check .`
- [ ] **Build**: `uv sync`
- [ ] **Test**: `uv run pytest`

## Stack & Architecture
- **Stack**: Python 3.13, FastAPI, HTMX, Jinja2, custom CSS (`app.css`).
- **Flow**: SSR HTML via HTMX without local JS state. Routes in `main.py`, logic in `game_*.py`.
- **Server**: `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Core Rules
- **No Simple Browser**: HTMX requires a full browser. Use: `"$BROWSER" http://localhost:8000`
- **Design/CSS**: Follow `.github/instructions/` (css-utilities & frontend-design).
- **Docs**: See `workshop/GUIDE.md`. Do not modify `workshop/` files unless directly asked.
