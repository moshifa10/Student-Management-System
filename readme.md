# 🎓 StudentDB — Flask CRUD Project

A complete beginner-friendly Flask project demonstrating full **CRUD** operations
using **SQLite** as the database.

---

## 📁 Project Structure

```
student_app/
├── app.py                  ← Main Flask application (all routes + DB logic)
├── requirements.txt        ← Dependencies
├── students.db             ← SQLite database (auto-created on first run)
└── templates/
    ├── base.html           ← Shared layout (nav, flash messages, styles)
    ├── index.html          ← READ  — List all students + search
    ├── form.html           ← CREATE/UPDATE — Add & Edit form (shared)
    ├── view.html           ← READ  — Single student detail page
    └── delete_confirm.html ← DELETE — Confirmation page
```

---

## ⚙️ Setup & Run

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in your browser
```
http://127.0.0.1:5000
```

The SQLite database (`students.db`) is created **automatically** on first run.

---

## 🔄 CRUD Operations

| Operation | HTTP Method | URL                  | What it does               |
|-----------|-------------|----------------------|----------------------------|
| **C**reate | GET        | `/add`               | Show the Add form          |
| **C**reate | POST       | `/add`               | Save new student to DB     |
| **R**ead   | GET        | `/`                  | List all students          |
| **R**ead   | GET        | `/student/<id>`      | View one student's details |
| **U**pdate | GET        | `/edit/<id>`         | Show pre-filled Edit form  |
| **U**pdate | POST       | `/edit/<id>`         | Save changes to DB         |
| **D**elete | GET        | `/delete/<id>`       | Confirmation page          |
| **D**elete | POST       | `/delete/<id>`       | Remove student from DB     |

---

## 🗄️ Database Schema

```sql
CREATE TABLE students (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT    NOT NULL,
    email      TEXT    NOT NULL UNIQUE,
    age        INTEGER NOT NULL,
    course     TEXT    NOT NULL,
    grade      TEXT    NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧠 Key Concepts Demonstrated

- **`sqlite3`** — Python's built-in SQLite library (no ORM needed)
- **`conn.row_factory = sqlite3.Row`** — Access columns by name, not index
- **Parameterised queries** (`?` placeholders) — Prevents SQL injection
- **Flask routes** — `GET` to display, `POST` to submit
- **`flash()`** — Show success/error messages across redirects
- **`redirect()` + `url_for()`** — Post/Redirect/Get pattern
- **Jinja2 templates** — Template inheritance with `{% extends %}`
- **`IntegrityError`** — Catch duplicate email errors gracefully