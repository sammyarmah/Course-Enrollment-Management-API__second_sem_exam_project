from fastapi import APIRouter, status, Depends, HTTPException
from app.services.course import CourseServices
from app.schema.course import CourseCreate, CourseUpdate
from app.api.deps import is_admin_user
from typing import Optional


course_router = APIRouter()

# creating a course
@course_router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(data_in: CourseCreate, user: int = Depends(is_admin_user)):
    return CourseServices.course_create(data_in)

# retrieving a course by id
@course_router.get("/{id}")
def get_course_by_id(id: int):
    course = CourseServices.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Course not found")
    return course

# retrieving all courses
@course_router.get("/")
def get_all_courses(title: Optional[str] = None):
    return CourseServices.get_all_courses(title)

# updating a course
@course_router.put("/{id}")
def update_course(id:int, course_data: CourseUpdate , user: int = Depends(is_admin_user)):
    course = CourseServices.update_course(id, course_data)

    if course is None:
        raise HTTPException(status_code=400, detail="Course not found")
    
    return {"message": "Course updated successfully", "data": course}

# deleting course
@course_router.delete("/{id}")
def delete_course(id:int, user: int = Depends(is_admin_user)):
    CourseServices.delete_course(id)
    return {"message": "Course deleted successfully"}

