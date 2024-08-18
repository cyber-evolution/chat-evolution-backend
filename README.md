# chat-evolution-backend
Always exist in this world and chat with you

## Requirements
+ python3.12.2

## Installation
+ Clone the project and change to the working directory

```bash
git clone git@github.com:cyber-evolution/chat-evolution-backend.git
cd chat-evolution-backend/
```
+ Manage virtual environments

```bash
pyenv local 3.12
pip install -U pip setuptools
pip install poetry
poetry install
poetry shell
```

## Start
```bash
fastapi dev app/main.py
```
## Project Tree
```
chat-evolution-backend
├─ .gitignore
├─ LICENSE
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ config
│  │  └─ __init__.py
│  ├─ crud
│  │  └─ __init__.py
│  ├─ dependdencies
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models
│  │  └─ __init__.py
│  ├─ routers
│  │  └─ __init__.py
│  └─ schemas
│     └─ __init__.py
├─ poetry.lock
└─ pyproject.toml

```