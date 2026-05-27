from flask import Flask, redirect, render_template
import sqlite3

def create_table(file_name: str):
    conn = sqlite3.connect(f"{file_name}.db")

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email NOT NULL UNIQUE,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL,
                    grade TEXT NOT NULL,
                )            
    """)
    print(f"Created a table {file_name}.db")
    conn.commit()


app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5000)
