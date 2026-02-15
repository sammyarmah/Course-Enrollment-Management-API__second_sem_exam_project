from fastapi import HTTPException, status
from typing import Optional
from app.schema.enrollment import EnrollmentCreate, Enrollment
from app.core.enrollment import enrollment_db

class EnrollmentServices:

    @staticmethod
    def enroll_student(data_in: EnrollmentCreate):
        for enrollment in enrollment_db.values():
            if (enrollment.user_id == data_in.user_id and enrollment.course_id == data_in.course_id):
                raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student already enrolled"
            )
        enrollment_id = len(enrollment_db) + 1

        new_enrollment = Enrollment(
           id = enrollment_id,
           user_id = data_in.user_id,
           course_id = data_in.course_id
       )
        enrollment_db[enrollment_id] = new_enrollment
        return new_enrollment
    
    @staticmethod
    def retrieve_student(id:int):
        enrolled_student = enrollment_db.get(id)
        if not enrolled_student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return enrolled_student
    
    @staticmethod
    def deregister_student(enrollment_id):
        enrolled_student = enrollment_db.get(enrollment_id)
        if not enrolled_student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        
        del enrollment_db[enrollment_id]

    @staticmethod
    def retrieve_enrollments(user_id: Optional[int] = None, course_id: Optional[int] = None):
        if not user_id and not course_id:
            return list(enrollment_db.values())
        
        enrollment_list = []

        if user_id:
            for enrollment in enrollment_db.values():
                if enrollment.user_id == user_id:
                    enrollment_list.append(enrollment) 

        if course_id:
            for enrollment in enrollment_db.values():
                if enrollment.course_id == course_id:
                    enrollment_list.append(enrollment)
        
        return enrollment_list

    @staticmethod
    def student_deregister(user_id: int, course_id: int):
        for id, enrollment in enrollment_db.items():
            if enrollment.user_id == user_id and enrollment.course_id == course_id:
                del enrollment_db[id]
                return
        

        
    
    

    