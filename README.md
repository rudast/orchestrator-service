# Orchestrator Service

Personal AI-powered orchestration service with Telegram as the main interface.

The goal of the project is to provide a single place for managing tasks, events, deadlines, notifications, and external integrations such as email, calendars, educational platforms, and other APIs.

This project is being developed primarily as:

- a learning project for practicing software engineering;
- a personal productivity tool.

## Vision

Orchestrator is not just a Telegram bot.

Telegram acts as the user interface, while the core of the system is responsible for:

- task management;
- calendar and event management;
- notifications and reminders;
- synchronization with external services;
- processing unstructured information with LLMs.

All external data sources are converted into a unified internal model.

## Planned Features

- Task management
- Calendar integration
- Email integration
- Educational platform integration
- Daily digests
- Smart notifications
- Natural language commands
- LLM-powered email and task processing

## Technology Stack

- Python 3.12+
- FastAPI
- aiogram 3
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- APScheduler / Arq / Celery
- Docker Compose
- Gemini API
- pytest
- ruff
- mypy
- GitHub Actions

## Project Status

Current milestone:

```text
v0.1.0 — Telegram Bot + Manual Tasks
```

Implemented:

- [ ] Telegram bot
- [ ] Manual task creation
- [ ] Task listing
- [ ] Project documentation

## Development Workflow

```text
Issue
↓
Branch
↓
Pull Request
↓
Review
↓
Merge
↓
Release
```

Every feature is developed through GitHub Issues and Pull Requests.

## Roadmap

### v0.1.0

- Telegram bot
- Manual task creation
- Task listing

### v0.2.0

- PostgreSQL
- Persistent task storage
- Database migrations

### v0.3.0

- Calendar and scheduling foundation

## Documentation

Project documentation is available in:

```text
/docs
```

## License

This project is currently developed for educational and personal use.