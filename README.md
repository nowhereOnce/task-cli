# Task-CLI

A professional command-line task manager built with Python. Organize your tasks efficiently from the terminal with an intuitive interface and persistent storage.

## Features

- ✅ **Create tasks** - Add new tasks with descriptions
- 📋 **List tasks** - View all tasks or filter by status (todo, in-progress, done)
- ✏️ **Update tasks** - Edit task descriptions with pre-filled input
- 🗑️ **Delete tasks** - Remove completed or unwanted tasks
- 🎯 **Track status** - Mark tasks as todo, in-progress, or done
- 💾 **Persistent storage** - Tasks are saved locally in `~/.task-cli/tasks.json`
- 🎨 **Rich formatting** - Beautiful colored tables and ASCII art banner

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd task-cli
```

2. Install the package:

```bash
pip install -e .
```

This will install the package in development mode along with dependencies.

## Usage

### Commands

#### Add a new task

```bash
task-cli add "Your task description"
```

#### List all tasks

```bash
task-cli list
```

#### List tasks by status

```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```

#### Update a task

```bash
task-cli update <task-id> "New description"
# or interactive mode (with pre-filled current description):
task-cli update <task-id>
```

#### Delete a task

```bash
task-cli delete <task-id>
```

#### Mark task as in progress

```bash
task-cli mark-in-progress <task-id>
```

#### Mark task as done

```bash
task-cli mark-done <task-id>
```

#### Mark task as todo

```bash
task-cli mark-todo <task-id>
```

## Project Structure

```plain-text
task-cli/
├── __init__.py           # Package initialization
├── app.py               # Main entry point
├── cli.py               # Command-line argument parser
├── database.py          # Task storage and retrieval
├── logic.py             # Business logic for task operations
└── utils.py             # Utility functions (banner, input handling)
```

## Dependencies

- **pyfiglet** - ASCII art text generation for banner
- **rich** - Beautiful terminal formatting and tables

See `requirements.txt` for version details.

## Data Storage

Tasks are stored in JSON format at `~/.task-cli/tasks.json`. Each task contains:

- `id` - Unique identifier
- `description` - Task description
- `status` - Current status (todo, in-progress, done)
- `createdAt` - Creation timestamp
- `updatedAt` - Last update timestamp (null if never updated)

## License

MIT License

## Author

Enrique Alejandro Aguilar Ramos