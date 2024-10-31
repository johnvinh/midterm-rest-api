# Midterm Rest API
This app uses Python and FastAPI.
## Installing Requirement
Run command:
`pip install -r requirements.txt`
## Running
Run command:
`uvicorn main:app --reload`
## Usage
The app will run on `http://localhost:8000`.
### Endpoints
GET /students: Retrieve a list of all students.

GET /students/{id}: Retrieve details of a student by ID.

POST /students: Add a new student.

PUT /students/{id}: Update an existing student by ID.

DELETE /students/{id}: Delete a student by ID.