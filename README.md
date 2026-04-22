🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# Soc Ops 🎯

> Turn any in-person mixer into a fun, fast social challenge.

Soc Ops is a Social Bingo game where players discover people who match each square, mark the board, and race for 5 in a row.

## Why this project is fun

- 🧊 **Great icebreaker** for team offsites, classes, and meetups
- ⚡ **Quick rounds** that keep energy high
- 🧠 **Simple game loop** built with FastAPI + Jinja templates
- 🧪 **Hands-on lab repo** for practicing GitHub Copilot agent workflows

## 🚀 Quick Start

```bash
pip install -e ".[dev]"
soc-ops
```

Then open [http://localhost:8000](http://localhost:8000) and start a round.

## 📚 Lab Guide

Follow the workshop from intro to multi-agent development:

| Part | Title |
|------|-------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development |

> 📝 Prefer offline reading? Use the guides in [`workshop/`](workshop/).

## 🛠️ Development

- Run tests: `pytest -q`
- Run linting: `ruff check .`
