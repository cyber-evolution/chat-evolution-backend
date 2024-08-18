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
│  ├─ api
│  │  ├─ __init__.py
│  │  ├─ config
│  │  │  ├─ __init__.py
│  │  │  └─ constant.py
│  │  ├─ crud
│  │  │  └─ __init__.py
│  │  ├─ dependdencies
│  │  │  └─ __init__.py
│  │  ├─ models
│  │  │  ├─ __init__.py
│  │  │  ├─ base.py
│  │  │  └─ user.py
│  │  ├─ routers
│  │  │  └─ __init__.py
│  │  └─ schemas
│  │     ├─ __init__.py
│  │     └─ user.py
│  └─ main.py
├─ poetry.lock
└─ pyproject.toml

```