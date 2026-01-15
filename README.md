# Python Flask Learning Repository

This repository contains a comprehensive collection of examples and tutorials for learning the Flask web framework in Python. It covers various aspects of Flask development, from basic routing to advanced topics like authentication, database integration, and REST APIs.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Directory Structure & Topics](#directory-structure--topics)
  - [Introduction](#introduction-1)
  - [Authentication](#authentication)
  - [Database](#database)
  - [Form Handling](#form-handling)
  - [HTTP Methods](#http-methods)
  - [Templates & Static Files](#templates--static-files)
  - [REST APIs](#rest-apis)
  - [SQL](#sql)
  - [Middlewares](#middlewares)
- [Usage](#usage)

## Introduction

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. This repository creates a structured learning path through different Flask capabilities.

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd python-flask
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The repository includes a `requirements.txt` file listing all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```

## Directory Structure & Topics

### Introduction
-   **Location:** `Introduction/`
-   **Content:** Basic Flask application structure, routing, dynamic URLs, variable rules, and URL building (`url_for`).
-   **Key File:** `main.py`

### Authentication
-   **Location:** `Authentication_in_Flask/`
-   **Content:** User session management, login/signup flows, and password hashing using `flask_login` and `workzeug`.
-   **Key Features:** Login, Sign Up, Home, Dashboard templates.

### Database
-   **Location:** `Database/`
-   **Content:** Integration examples with various databases.
    -   `flask_sqlite`: Using SQLite with Flask.
    -   `flask_mongodb`: Connection to MongoDB.
    -   `flask_mySQL`: Connection to MySQL.
    -   `flask_postgreSQL`: Connection to PostgreSQL.

### Form Handling
-   **Location:** `Form_Handling/`
-   **Content:** Handling user input securely and efficiently.
    -   `flask_WTF`: Using Flask-WTF for form validation and rendering.
    -   `file_uploads`: Handling file uploads from users.
    -   `csrf_attacks`: Understanding and preventing Cross-Site Request Forgery (CSRF).

### HTTP Methods
-   **Location:** `HTTP_Methods/`
-   **Content:** Examples demonstrating different HTTP methods (GET, POST, PUT, DELETE) within Flask routes.

### Templates & Static Files
-   **Location:** `Templates_&&_Static/`
-   **Content:** 
    -   `flask_render_template`: Rendering HTML templates.
    -   `template_inheritance`: Using Jinja2 template inheritance (base templates, child templates) to maintain consistent layout.

### REST APIs
-   **Location:** `Rest_APIs/`
-   **Content:** Building RESTful APIs using Flask, likely utilizing extensions like `Flask-RESTful` or standard Flask routes to return JSON data.

### SQL
-   **Location:** `SQL/`
-   **Content:** Direct SQL interaction or SQLAlchemy ORM examples managed specifically for SQL operations.

### Middlewares
-   **Location:** `Middlewares/`
-   **Content:** Implementing middleware to hook into the request/response lifecycle (e.g., logging, request preprocessing).

### Others
-   **Heroku:** Deployment configurations/examples for Heroku.
-   **JsonHandling:** specialized JSON manipulation examples.

## Usage

To run any of the examples:

1.  Navigate to the specific directory of the topic you are interested in.
    ```bash
    cd Authentication_in_Flask
    ```

2.  Run the application file (usually `app.py` or `main.py`).
    ```bash
    python app.py
    ```

3.  Open your web browser and go to the local server address shown in the terminal (usually `http://127.0.0.1:5000` or `http://localhost:5000`).

## Dependencies

Key libraries used in this project include:
-   `flask`: The core web framework.
-   `flask-cors`: Handling Cross-Origin Resource Sharing.
-   `requests`: Sending HTTP requests.
-   `flask-sqlalchemy`: ORM for database interactions.
-   `flask-WTF`: Form handling and validation.
-   `db-sqlite3`: SQLite connector.
-   `flask_login`: User session management.
-   `werkzeug`: WSGI utility library (security/hashing).
-   `Flask-RESTful`: Building REST APIs.
-   `gunicorn`: WSGI HTTP Server.

Make sure to install them using:
```bash
pip install -r requirements.txt
```
