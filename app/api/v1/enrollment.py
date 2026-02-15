from fastapi import APIRouter, Depends, status, HTTPException
from app.schema.enrollment import EnrollmentCreate
from app.services.enrollment import EnrollmentServices
from app.api.deps import is_admin_user
from app.api.deps import is_student_user
from typing import Optional


enrollment_router = APIRouter()

# ------------------------------------
#        STUDENT ENDPOINTS
# ------------------------------------
@enrollment_router.post("/", status_code=status.HTTP_201_CREATED)
def enroll_student(data_in: EnrollmentCreate, user: int = Depends(is_student_user)):
    return EnrollmentServices.enroll_student(data_in)

@enrollment_router.get("/{id}")
def retrieve_student(id:int, user: int = Depends(is_student_user)):
    return EnrollmentServices.retrieve_student(id)

@enrollment_router.delete("/{id}")
def deregister_student(id:int, user: int = Depends(is_student_user)):
    EnrollmentServices.deregister_student(id)
    return {"Student deregistered successfully"}

# -------------------------------------------
#             ADMIN ENDPOINTS
# -------------------------------------------

# retrieve all enrollments by admin
@enrollment_router.get("/")
def retrieve_enrollments(
    user_id: Optional[int] = None,
    course_id: Optional[int] = None,
    admin: int = Depends(is_admin_user)
    ):
    return EnrollmentServices.retrieve_enrollments(user_id, course_id)

@enrollment_router.get("/course/{course_id}")
def retrieve_enrollments(course_id:int, user: int = Depends(is_admin_user)):
    course = EnrollmentServices.retrieve_enrollments(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@enrollment_router.delete("/{user_id}/{course_id}")
def student_deregister(user_id, course_id, user: int = Depends(is_admin_user)):
    EnrollmentServices.student_deregister(user_id, course_id)
    return {"message": "Student deregistered successfully"}
    






