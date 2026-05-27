import sqlite3

class DataBase():

    def __init__(self, fileName: str, table: str):
 
        self.file_name = fileName.lower().strip()
        self.table_name = table.lower().strip()

        # Connect DB
        self.conn = sqlite3.connect(f"{fileName}.db")
        self.cursor = self.conn.cursor()


    
    def get_students(self) -> list[dict]: #list[tuple[str, str, int]]:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        all_students = self.cursor.fetchall()
        if len(all_students) < 1:
            return None
        students = []
        for student in all_students:
            no_id, name, email, age, course, grade = student
            fields = {
                "id": no_id,
                "name": name,
                "email" : email,
                "age": age,
                "course" : course,
                "grade" : grade
            }
            students.append(fields)
        return students
        

    def add_member(self, name: str, email: str, age: int, course: str, grade: str) -> bool:
        values = (name, email, age, course, grade)

        self.cursor.execute(f"INSERT INTO {self.table_name} (name, email, age, course, grade) VALUES (?,?,?,?,?)", values)
        self.conn.commit()
        self.conn.close()
        return True
    

    def get_student(self, studentId: int) -> tuple:
        self.cursor.execute(f""" SELECT * FROM {self.table_name} WHERE id = {studentId} LIMIT 1""")

        student = self.cursor.fetchone()

        if(student):
            self.conn.commit()
            self.conn.close()

            return student
        
        else:
            return None
        