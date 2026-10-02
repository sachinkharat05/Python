# Student Management System

A small student-record management application built with Python, Flask, SQLite, and Bootstrap. It provides a browser-based interface for adding, viewing, searching, editing, and deleting student records.

## Features

- Create, view, update, and delete student records.
- Search records by student name, email address, or course.
- Require a name, a valid email address, and a course; phone number is optional.
- Prevent duplicate email addresses using a unique database constraint.
- Ask for confirmation before deleting a record.
- Store data locally in a SQLite database.
- Use parameterized SQL queries for database operations.

## Requirements

- Python 3.9 or later
- `pip`
- An internet connection when loading the Bootstrap stylesheet and JavaScript from the CDN

## Setup and Run

Open a terminal in the project directory, then create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell prevents activation, use Command Prompt instead:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python app.py
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The application creates the `students.db` SQLite database and its `students` table when it starts. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

Stop the development server with `Ctrl+C`. To leave the virtual environment, run `deactivate`.

## Project Structure

```text
student_crud/
├── app.py                 # Flask routes and SQLite database operations
├── requirements.txt       # Python package requirements
├── README.md              # Setup and project documentation
└── templates/
   ├── base.html          # Shared page layout and flash messages
   ├── index.html         # Student list, search, and row actions
   └── form.html          # Add and edit student form
```

## Application Flow

1. `app.py` creates the Flask application and initializes the SQLite schema when run directly.
2. The `/` page reads student records from SQLite. An optional `q` query parameter filters results by name, email, or course.
3. The `/add` and `/edit/<student_id>` routes display the shared form and process submitted values.
4. The `/delete/<student_id>` route accepts a POST request and removes the selected record.
5. The templates render the pages, while Flask flash messages report successful actions and validation errors.

## Routes

| Method | URL | Purpose |
| --- | --- | --- |
| `GET` | `/` | List all students or search with `?q=term` |
| `GET`, `POST` | `/add` | Display the add form and create a student |
| `GET`, `POST` | `/edit/<student_id>` | Display the edit form and update a student |
| `POST` | `/delete/<student_id>` | Delete a student |

## Data and Validation

The `students` table contains:

| Column | Type | Rules |
| --- | --- | --- |
| `id` | Integer | Auto-incrementing primary key |
| `name` | Text | Required |
| `email` | Text | Required and unique |
| `phone` | Text | Optional |
| `course` | Text | Required |

Required values are checked by both the browser form and the Flask routes. SQLite enforces unique email addresses, and the application displays a message if an address is already in use. Search and write queries use SQL parameters rather than inserting submitted values into SQL strings.

## Configuration and Notes

- The database file is named `students.db` and is created in the current working directory when `python app.py` starts. Keep a copy of this file if you need to preserve the records.
- Bootstrap assets are loaded from jsDelivr, so the page still needs internet access for Bootstrap styling and dismissible alerts.
- The application currently has no login or access control. Run it only in a trusted environment.
- `app.py` enables Flask debug mode for local development. Turn debug mode off and use a production WSGI server before deploying the application.
- Replace the example `app.secret_key` value with a securely generated secret before deployment. Do not commit production secrets to source control.
