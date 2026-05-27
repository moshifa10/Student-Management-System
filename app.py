from flask import Flask, render_template, redirect
import sqlite3
import argparse
import os
from students import DataBase


def main():
    parser = argparse.ArgumentParser(
        description="I am Testing Database if I do understand it."
    )

    parser.add_argument(
        "-f","--filename",
        default="students",
        help="Type the filename for a Database"
    )

    parser.add_argument(
        "-t","--table",
        default="students",
        help="Type the TableName for a Database"
    )

    args = parser.parse_args()
    return args.filename, args.table




def create_table(file_name: str, table_name: str):
    conn = sqlite3.connect(f"{file_name}.db")

    cursor = conn.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email NOT NULL ,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL,
                    grade TEXT NOT NULL
                )            
    """)

    cursor.execute(f"INSERT INTO {table_name} (name, email, age, course, grade) VALUES (?,?,?,?,?)", ("Njabs", "mo@gmail.com", 18, "Accounting", "12"))
    print(f"Created a Database {file_name}.db")
    print(f"Created a table {table_name}")
    conn.commit()

    conn.close()


app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def list_all_students():
    filename, tablename = main()
    data_base = DataBase(fileName=filename, table=tablename)
    students_ = data_base.get_students()
    print(students_)

    if students_ == None:
        return render_template("no_students.html"), 404

    return render_template("index.html", all_students=students_), 200

if __name__ == "__main__":
    
    filename, tablename = main()
    if not os.path.isfile(filename):
        create_table(file_name=filename, table_name=tablename)

    
    app.run(host="localhost", debug=True, port=5000)
