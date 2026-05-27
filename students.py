import sqlite3

class DataBase():

    def __init__(self, fileName: str, table: str):
 
        self.file_name = fileName.lower().strip()
        self.table_name = table.lower().strip()

        # Connect DB
        conn = sqlite3.connect(f"{fileName}.db")
        self.cursor = conn.cursor()


    
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
        
