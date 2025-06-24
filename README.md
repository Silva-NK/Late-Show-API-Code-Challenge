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
6. Finally to run use `flask run`.

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


## Route Summary

1. Landing Page : `/` : Opens landing page  
2. POST : `/register` : Register a new user  
3. POST : `/login` : Login and receive a token  
4. GET : `/profile` : Get logged-in user details (requires token)  
5. GET : `/episodes` : List all episodes  
6. GET : `/episodes/<id>` : Retrieve one episode & its appearances  
7. DELETE : `/episodes/<id>` : Delete an episode and its appearances (requires token)  
8. GET : `/guests` : List all guests  
9. POST : `/appearances` : Create guest appearance for an episode (requires token)


## Example Requests & Responses

1. **Register User** — `/register`  
   **Register a new user**  
   **Request Body:**
   ```json
   {
     "username": "janeysmith",
     "password": "password123"
   }
   ```
   **Success Response (201):**
   ```json
   {
     "message": "User registered successfully"
   }
   ```
   **Failure (Username exists):**
   ```json
   {
     "error": "Username already exists"
   }
   ```

2. **Login User** — `/login`  
   **Log in as existing user**  
   **Request Body:**
   ```json
   {
     "username": "janeysmith",
     "password": "password123"
   }
   ```
   **Success Response (200):**
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIsI..."
   }
   ```
   **Failure (Invalid credentials):**
   ```json
   {
     "error": "Invalid credentials"
   }
   ```

3. **Get Profile** — `/profile`  
   **Get authenticated user's profile (Auth Required)**  
   **Headers:**
   ```
   Authorization: Bearer <access_token>
   ```
   **Success Response (200):**
   ```json
   {
     "id": 1,
     "username": "janeysmith"
   }
   ```

4. **List All Episodes** — `/episodes`  
   **Response (200):**
   ```json
   [
     {
       "appearances": [
      {
        "episode_id": 1,
        "guest": {
          "appearances": [
            {
              "episode_id": 1,
              "guest_id": 1,
              "id": 1,
              "rating": 5
            },
            {
              "episode_id": 4,
              "guest_id": 1,
              "id": 6,
              "rating": 2
            }
          ],
          "id": 1,
          "name": "Zendaya",
          "occupation": "Actor"
        },
        "guest_id": 1,
        "id": 1,
        "rating": 5
      },...
     }
   ]
   ```

5. **Get Episode by ID** — `/episodes/1`  
   **Success Response (200):**
   ```json
   {
     "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "appearances": [
          {
            "episode_id": 1,
            "guest_id": 1,
            "id": 1,
            "rating": 5
          },
          {
            "episode_id": 4,
            "guest_id": 1,
            "id": 6,
            "rating": 2
          }
        ],
        "id": 1,
        "name": "Zendaya",
        "occupation": "Actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 5
    },...
   }
   ```
   **Failure Response (404):**
   ```json
   {
     "error": "Episode not found"
   }
   ```

6. **Delete Episode by ID** — `/episodes/1`  
   **(Auth Required)**  
   **Headers:**
   ```
   Authorization: Bearer <access_token>
   ```
   **Success Response (200):**
   ```json
   {
     "message": "Episode 1 deleted"
   }
   ```
   **Failure Response (404):**
   ```json
   {
     "error": "Episode not found"
   }
   ```

7. **List All Guests** — `/guests`  
   **Response (200):**
   ```json
   [
     {
       "appearances": [
            {
                "episode_id": 1,
                "guest_id": 1,
                "id": 1,
                "rating": 5
            },
            {
                "episode_id": 4,
                "guest_id": 1,
                "id": 6,
                "rating": 2
            }
            ],
            "id": 1,
            "name": "Zendaya",
            "occupation": "Actor"
        },
        {
            "appearances": [
            {
                "episode_id": 1,
                "guest_id": 2,
                "id": 2,
                "rating": 4
            },
            {
                "episode_id": 5,
                "guest_id": 2,
                "id": 7,
                "rating": 5
            }
            ],
            "id": 2,
            "name": "Pedro Pascal",
            "occupation": "Actor"
        },...
     }
   ]
   ```

8. **Create Appearance** — `/appearances`  
   **(Auth Required)**  
   **Headers:**
   ```
   Content-Type: application/json  
   Authorization: Bearer <access_token>
   ```
   **Request Body:**
   ```json
   {
     "rating": 4,
     "guest_id": 1,
     "episode_id": 1
   }
   ```
   **Success Response (201):**
   ```json
   {
     "id": 1,
     "rating": 4,
     "guest_id": 1,
     "episode_id": 1,
     "guest": {
       "id": 1,
       "name": "Zendaya",
       "occupation": "Actor"
     }
   }
   ```
   **Failure (Missing fields):**
   ```json
   {
     "error": "rating, guest_id, and episode_id are required."
   }
   ```
   **Failure (Rating out of range):**
   ```json
   {
     "error": "Rating must be an integer between 1 and 5"
   }
   ```
   **Failure (Guest not found):**
   ```json
   {
     "error": "Guest not found."
   }
   ```
   **Failure (Episode not found):**
   ```json
   {
     "error": "Episode not found."
   }
   ```


## Using Postman

The file `challenge-4-lateshow.postman_collection.json` contains a pre-configured Postman collection for testing this API.

To use Postman:

1. Open Postman.
2. Click **Import**.
3. Select the file `challenge-4-lateshow.postman_collection.json` (or drag and drop it into the import box).
4. Ensure the base URL is set to `http://localhost:5555/` (or `http://127.0.0.1:5555/`).
5. Click **Send** to test each route.

> **Make sure the server is running** before testing. Run it with:
```bash
flask run
```

6. Use the imported collection to test endpoints. Click **Send** on any request.

> **Note:** Authenticated routes like `/profile`, `DELETE /episodes/<id>`, and `POST /appearances` require a valid token.

### To test protected routes:

1. First, register or log in via the `/register` or `/login` endpoint.
2. Copy the `access_token` returned in the login response.
3. Go to the **Headers** tab of any protected route request.
4. Add the following header:

   ```
   Key: Authorization
   Value: Bearer <your_access_token>
   ```

Example:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsI...
```

> Don't forget to include the word `Bearer` before the token value.


## Resources

- [Late-Show-API-Code-Challenge Git Repo](https://github.com/Silva-NK/Late-Show-API-Code-Challenge)
