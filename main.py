from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Base model without id
class StudentBase(BaseModel):
    name: str
    grade: str
    email: str

# Model for creating a student (input model)
class StudentCreate(StudentBase):
    pass

# Model for returning a student (output model with id)
class Student(StudentBase):
    id: int

# In-memory "database" and auto-incrementing id counter
students = {}
next_id = 1

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

# POST /students: Add a new student without requiring an id
@app.post("/students")
def create_student(student: StudentCreate):
    global next_id
    student_id = next_id
    next_id += 1
    new_student = Student(id=student_id, **student.dict())
    students[student_id] = new_student
    return new_student

# PUT /students/{id}: Update an existing student by ID
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentBase):
    if student_id in students:
        updated_student = Student(id=student_id, **student.dict())
        students[student_id] = updated_student
        return updated_student
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
