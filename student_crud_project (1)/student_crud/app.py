import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, g

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DATABASE = "students.db"


# ---------- Database helpers ----------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                name   TEXT NOT NULL,
                email  TEXT UNIQUE NOT NULL,
                phone  TEXT,
                course TEXT NOT NULL
            )
            """
        )


# ---------- READ (list + search) ----------
@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    db = get_db()
    if q:
        students = db.execute(
            "SELECT * FROM students WHERE name LIKE ? OR email LIKE ? OR course LIKE ? ORDER BY id DESC",
            (f"%{q}%", f"%{q}%", f"%{q}%"),
        ).fetchall()
    else:
        students = db.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return render_template("index.html", students=students, q=q)


# ---------- CREATE ----------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not course:
            flash("Name, email, and course are required.", "danger")
            return render_template("form.html", student=request.form, title="Add Student")

        try:
            db = get_db()
            db.execute(
                "INSERT INTO students (name, email, phone, course) VALUES (?, ?, ?, ?)",
                (name, email, phone, course),
            )
            db.commit()
            flash("Student added successfully.", "success")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("That email address is already in use.", "danger")
            return render_template("form.html", student=request.form, title="Add Student")

    return render_template("form.html", student={}, title="Add Student")


# ---------- UPDATE ----------
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    db = get_db()
    student = db.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    if student is None:
        flash("Student not found.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not course:
            flash("Name, email, and course are required.", "danger")
            return render_template("form.html", student=request.form, title="Edit Student")

        try:
            db.execute(
                "UPDATE students SET name=?, email=?, phone=?, course=? WHERE id=?",
                (name, email, phone, course, student_id),
            )
            db.commit()
            flash("Student updated successfully.", "success")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("That email address is already in use.", "danger")
            return render_template("form.html", student=request.form, title="Edit Student")

    return render_template("form.html", student=student, title="Edit Student")


# ---------- DELETE ----------
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id = ?", (student_id,))
    db.commit()
    flash("Student deleted successfully.", "warning")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
