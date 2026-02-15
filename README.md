# Course-Enrollment-Management-API


## Overview

The **Course Enrollment Management API** is a FastAPI-based backend application designed to manage users, courses, and student enrollments. It provides RESTful endpoints for students to enroll in courses and deregister, and for administrators to manage and view enrollments.

This project demonstrates proper backend architecture using:

* FastAPI for API development
* Pydantic for schema validation
* Service layer for business logic
* Dependency injection for role-based access
* Pytest for automated testing
* In-memory database for simplicity and test isolation

---

## Project Structure

```
Course-Enrollment-Management-API/
│
├── app/
│   ├── main.py                  
│   │
│   ├── api/
│   │   ├── deps.py             
│   │   └── v1/
│   │       ├── user.py         
│   │       ├── course.py       
│   │       └── enrollment.py   
│   │
│   ├── core/
│   │   ├── user.py            
│   │   ├── course.py           
│   │   └── enrollment.py    
│   │
│   ├── schema/
│   │   ├── user.py            
│   │   ├── course.py           
│   │   └── enrollment.py       
│   │
│   └── services/
│       ├── user.py             
│       ├── course.py         
│       └── enrollment.py      
│
├── test/
│   ├── api/
│   │   ├── test_user.py
│   │   ├── test_course.py
│   │   └── test_enrollment.py
│   │
│   └── conftest.py            
│          
├── README.md                  
└── .gitignore
```

---

## Features

### Student Features

* Enroll in a course
* View enrollment details
* Deregister from a course

### Admin Features

* View all enrollments
* View enrollments by specific course
* Force student deregistration

### System Features

* Role-based access control
* Service-layer architecture
* Automated testing with pytest
* Clean and modular structure

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Course-Enrollment-Management-API
```

### 2. Create and activate virtual environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn pytest
```

---

## Running the API

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

You should see output like:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## Access API Documentation

FastAPI automatically provides interactive documentation:

Swagger UI:

```
http://127.0.0.1:8000/docs
```

You can test endpoints directly from the browser.

---

## Running Tests

This project uses **pytest** for automated testing.

Run all tests:

```bash
pytest -v
```

Example output:

```
15 passed in 0.90s
```

---

## Test Isolation

The project uses an in-memory database implemented as Python dictionaries.

To ensure proper test isolation, the test database is automatically cleared before each test using this fixture:

```python
@pytest.fixture(autouse=True)
def clear_enrollment_db():
    enrollment_db.clear()
```

This ensures:

* No shared state between tests
* Reliable and repeatable test results

---

## Running a Specific Test File

```bash
pytest test/api/test_enrollment.py -v
```

Run a specific test function:

```bash
pytest -k test_enroll_student -v
```

---

## API Base URL

```
http://127.0.0.1:8000
```

---

## Example Endpoints

### Enroll Student

```
POST /enrollments/
```

### Get Enrollment

```
GET /enrollments/{id}
```

### Deregister Student

```
DELETE /enrollments/{id}
```

### View All Enrollments (Admin)

```
GET /enrollments/
```

---

## Technologies Used

* FastAPI
* Python 3.10+
* Pytest
* Uvicorn
* Pydantic

---

## Development Best Practices Used

* Separation of concerns (Router, Service, Schema, Core)
* Dependency injection
* Test isolation
* RESTful API design
* Modular architecture

---

## Author

Samuel Amartey Armah

---

## License

This project is for educational and demonstration purposes.

---

## Future Improvements

* Add database integration (PostgreSQL)
* Add authentication (JWT)
* Add Docker support
* Add CI/CD pipeline

---

**End of Documentation**
