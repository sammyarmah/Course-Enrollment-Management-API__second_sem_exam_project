from fastapi import HTTPException
from app.schema.user import UserCreate, User
from app.core.user import user_db



class UserServices:
    
    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(user_db) + 1

        new_user = User(
            id = user_id,
            name = user_data.name,
            email = user_data.email,
            role = user_data.role
        )
        user_db[user_id] = new_user

        return new_user
    
    @staticmethod   
    def get_user_by_id(id:int):
        user = user_db.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    @staticmethod
    def get_all_users():
        return list(user_db.values())

