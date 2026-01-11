from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

DB_NAME = "database.db"

# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        rating INTEGER,
        comments TEXT,
        date_submitted TEXT
    )
    """)
    conn.commit()
    conn.close()

create_table()

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    rating = request.form["rating"]
    comments = request.form["comments"]

    conn = get_db()
    conn.execute("""
        INSERT INTO feedback (name, email, rating, comments, date_submitted)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, rating, comments, datetime.now()))
    conn.commit()
    conn.close()

    return redirect("/")

# ---------- ADMIN LOGIN ----------
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin":
            session["admin"] = True
            return redirect("/admin-dashboard")
        else:
            return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")

# ---------- ADMIN DASHBOARD ----------
@app.route("/admin-dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin-login")

    conn = get_db()
    data = conn.execute("SELECT * FROM feedback").fetchall()
    conn.close()

    total = len(data)
    avg = round(sum([row["rating"] for row in data]) / total, 2) if total else 0

    return render_template("admin.html", feedback=data, total=total, avg=avg)

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
