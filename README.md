# LATE SHOW API CODE CHALLENGE

## Introduction

Late Show API is a lightweight RESTful backend built with Flask, SQLAlchemy, and PostgreSQL. It models a late night TV show system with full CRUD and JWT-authenticated endpoints for managing episodes, guests, and guest appearances. Authentication is required for modifying data, ensuring secure access to protected routes.

## MVC Structure

.
├── challenge-4-lateshow.postman_collection.json
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 69e98ae1b12d_initial_migration.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── server
    ├── app.py
    ├── config.py
    ├── controllers
    │   ├── appearance_controller.py
    │   ├── auth_controller.py
    │   ├── episode_controller.py
    │   ├── guest_controller.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── appearance_controller.cpython-312.pyc
    │       ├── auth_controller.cpython-312.pyc
    │       ├── episode_controller.cpython-312.pyc
    │       ├── guest_controller.cpython-312.pyc
    │       └── __init__.cpython-312.pyc
    ├── extensions.py
    ├── models
    │   ├── appearance.py
    │   ├── episode.py
    │   ├── guest.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── appearance.cpython-312.pyc
    │   │   ├── episode.cpython-312.pyc
    │   │   ├── guest.cpython-312.pyc
    │   │   ├── __init__.cpython-312.pyc
    │   │   └── user.cpython-312.pyc
    │   └── user.py
    ├── __pycache__
    │   ├── app.cpython-312.pyc
    │   ├── config.cpython-312.pyc
    │   ├── extensions.cpython-312.pyc
    │   └── seed.cpython-312.pyc
    └── seed.py

9 directories, 37 files



## Setup Instructions

1. Clone the repository.
2. Ensure PostgreSQL is installed and running.
3. Create a database, e.g., `late_show_db`.
4. Set up your environment:
    ```bash
    pipenv install
    pipenv shell
    export FLASK_APP=server.app:create_app
    export FLASK_RUN_PORT=5555
    ```
5. Add a `.env` file with:
    ```env
    DATABASE_URL=postgresql://<user>:<password>@localhost:5432/late_show_db
    JWT_SECRET_KEY=dev-super-secret-key
    JWT_ACCESS_TOKEN_EXPIRES=3600
    ```

## Database Migration & Seeding

To migrate and create tables:
```bash
flask db init      # (NOTE: Run only once)
flask db migrate -m "Initial migration"
flask db upgrade

If you wish to make use of the seed data in seed.py:
- Run `python -m server.seed`

If you wish to use the Flask shell, use:
- Run `flask shell`
```


## Resources

- [Late-Show-API-Code-Challenge Git Repo](https://github.com/Silva-NK/Late-Show-API-Code-Challenge)

FLASK_APP=server.app:create_app
FLASK_ENV=development
FLASK_RUN_PORT=5555