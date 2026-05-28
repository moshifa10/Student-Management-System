from flask import Flask, render_template, redirect, request, url_for, flash
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

    # cursor.execute(f"INSERT INTO {table_name} (name, email, age, course, grade) VALUES (?,?,?,?,?)", ("Njabs", "mo@gmail.com", 18, "Accounting", "12"))
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

@app.route("/add", methods=["GET", "POST"])
def add():
    filename, tablename = main()
    if request.method.lower() == "get":
        return render_template("form.html"),201

    if request.method.lower() == "post":
        
        if len(request.form) == 5:
            name = request.form.get("name")
            email = request.form.get("email")
            age = int(request.form.get("age"))
            course = request.form.get("course")
            grade = request.form.get("grade")

            data_base = DataBase(fileName=filename, table=tablename)

            data_base.add_member(name,email,age,course,grade)

    return redirect(url_for("list_all_students"))

@app.route("/student/<int:id>")
def get_learner(id : int):
    data_base = DataBase(fileName=filename, table=tablename)    
    student = data_base.get_student(id)

    if student == None:
        return render_template("no_students.html"), 404
    
    print(student)
    return render_template("view.html", student=student)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    data_base = DataBase(fileName=filename, table=tablename)    
    student = data_base.get_student(id)
    if student == None:
        return render_template("no_students.html"), 404
    
    if request.method == "GET":
        return render_template("edit_forms.html", student=student)
    
    elif request.method == "POST":  
        if len(request.form) == 5:
            name = request.form.get("name")
            email = request.form.get("email")
            age = int(request.form.get("age"))
            course = request.form.get("course")
            grade = request.form.get("grade")

            data_base = DataBase(fileName=filename, table=tablename)

            data_base.edit(id,name,email,age, course, grade)
            return redirect(url_for("list_all_students"))
        
        return render_template("no_students.html")
    
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):

    if request.method == "GET":
        return render_template("delete_confirm.html",student=id)
    
    elif request.method == "POST":
        data_base = DataBase(fileName=filename, table=tablename)

        data_base.delete(id)
        return redirect(url_for("list_all_students"))









if __name__ == "__main__":
    
    filename, tablename = main()
    if not os.path.isfile(filename):
        create_table(file_name=filename, table_name=tablename)
    app.run(host="localhost", debug=True, port=5000)
