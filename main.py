from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Student model
class Student(BaseModel):
    id: int
    name: str
    grade: str
    email: str

# In-memory "database"
students = {}

# GET /students: Retrieve a list of all students
@app.get("/students")
def get_students():
    return list(students.values())

# GET /students/{id}: Retrieve a student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# POST /students: Add a new student
@app.post("/students")
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    students[student.id] = student
    return student

# PUT /students/{id}: Update an existing student by ID
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id in students:
        students[student_id] = student
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# DELETE /students/{id}: Delete a student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
