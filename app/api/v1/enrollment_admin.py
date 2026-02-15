from fastapi import APIRouter, Depends, status, HTTPException
from app.services.enrollment import EnrollmentServices
from app.api.deps import is_admin_user
from typing import Optional

enrollment_router = APIRouter()


# retrieve all enrollments by admin
@enrollment_router.get("/")
def retrieve_enrollments(
    user_id: Optional[int] = None,
    course_id: Optional[int] = None,
    user: int = Depends(is_admin_user)
    ):
    return EnrollmentServices.retrieve_enrollments(user_id, course_id)

@enrollment_router.get("/{course_id}")
def retrieve_enrollment_by_course(course_id:int, user: int = Depends(is_admin_user)):
    course = EnrollmentServices.retrieve_enrollment_by_course(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@enrollment_router.delete("/{user_id}/{course_id}")
def deregistration(user_id, course_id, user: int = Depends(is_admin_user)):
    return EnrollmentServices.deregistration(user_id, course_id)
    
