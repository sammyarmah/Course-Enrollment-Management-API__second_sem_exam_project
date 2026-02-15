from fastapi import APIRouter, Depends, status
from app.schema.enrollment import EnrollmentCreate
from app.services.enrollment import EnrollmentServices
from app.api.deps import is_student_user


enrollment_router = APIRouter()

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






