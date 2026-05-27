from flask import Flask
import sqlite3
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description="I am Testing Database if I do understand it."
    )

    parser.add_argument(
        "-f","--filename",
        default="students",
        help="Type the filename for a Database"
    )

    args = parser.parse_args()
    return args.filename




def create_table(file_name: str):
    conn = sqlite3.connect(f"{file_name}.db")

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email NOT NULL UNIQUE,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL,
                    grade TEXT NOT NULL
                )            
    """)
    print(f"Created a table {file_name}.db")
    conn.commit()


app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    
    filename = main()
    if not os.path.isfile(filename):
        create_table(file_name=filename)
    app.run(host="localhost", debug=True, port=5000)
