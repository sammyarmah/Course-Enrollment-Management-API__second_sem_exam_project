from fastapi import HTTPException, status
from app.schema.user import UserRole, User
from app.services.user import UserServices

def is_admin_user(user_id: int):
    user: User = UserServices.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "User not found")
    
    if not user.role == UserRole.admin:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN, 
            detail= "You do not have permission to perform this action"
        )
    
def is_student_user(user_id: int):
    user: User = UserServices.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User cannot be found"
        )
    
    if not user.role == UserRole.student:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "You do not have permission to perform this action"
        )
     