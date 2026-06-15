# Bot Architecture

## Purpose

Telegram bot is interface layer of project. It helps with interaction between user and orchestrator. It has a few
commands
for working with tasks.

## Entry point

```text
main.py
-> setup_logging()
-> config = get_config()
-> startup()
-> dispatcher = Dispatcher()
-> bot = Bot()
-> routers
-> polling
```

## Current project structure

```text
app/    
    bot/
        handlers/   # Files with handlers
        settings.py # Setup up bot and polling
    models/         # Pydantic models
        task.py     
    services/        # Services for handling
        task.py
    utils/          # Another tools
        logging.py       
```

## Bot startup flow

Bot and Dispatcher are created in app/bot/settings.py. List of routers must be in the same file. Polling starts in
`app/bot/settings.py`, in the same place session is closed.

## Handlers

Files with handlers: `/app/bot/handlers`

```text
app/bot/handlers/
                start.py
                task.py
```

start.py has handler that processes the /start command. While task.py process all task-related commands that interact
with task managing.

## Services

### TaskService

TaskService has few methods for managing tasks. It uses temporary storage for tasks. It can create, list and delete
tasks.

## Commands

| Command               | Responsibility                               |
|-----------------------|----------------------------------------------|
| /start                | Sends initial greeting                       |
| /task <title>         | Creates a task                               |
| /tasks                | Shows current user's tasks                   |
| /delete_task <number> | Deletes task by number from user's task list |

## How to add a new command

1. Add new router if it's necessary
2. Connect this router with dispatcher
3. Add or update handler
4. Connect handler to router
5. Add new service if it's necessary
6. Update docs
7. Update this document

## Current limitations

- Tasks are stored in memory.
- Bot currently uses polling.
- Commands are simple text commands.
- No persistence between restarts.
