from fastapi import HTTPException, status
from app.schema.course import CourseCreate, Course, CourseUpdate
from app.core.course import course_db
from typing import Optional


class CourseServices:

    @staticmethod
    def course_create(data_in: CourseCreate):
        if not data_in.title and not data_in.code:
            raise ValueError("Title is required")
        
        for course in course_db.values():
            if course.code == data_in.code:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Course already exists")
        
        course_id = len(course_db) + 1

        new_course = Course(
            id = course_id,
            title = data_in.title,
            code = data_in.code
        )
        course_db[course_id] = new_course
        return new_course
    
    @staticmethod
    def get_course_by_id(course_id):
        return course_db.get(course_id)
    
    @staticmethod
    def get_all_courses(title: Optional[str] = None):
        if not title:
            return list(course_db.values())
        
        course_list = []

        if title:
            for course in course_db.values():
                if course.title == title:
                    course_list.append(course)

        return course_list
    
    @staticmethod
    def update_course(course_id:int, course_data: CourseUpdate):
        course = course_db.get(course_id)
        if course is None:
            return {"message": "Course not found", "data": []}

        if course_data.title:
            course.title = course_data.title

        if course_data.code:
            course.code = course_data.code

        return course
 
    @staticmethod
    def delete_course(course_id: int):
        course = course_db.get(course_id)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        
        del course_db[course_id]

    