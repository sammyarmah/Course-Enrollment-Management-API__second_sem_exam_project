from fastapi import APIRouter, status, HTTPException
from app.schema.user import UserCreate, User
from app.services.user import UserServices


user_router = APIRouter()

# creating a user
@user_router.post("/", status_code= status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    return UserServices.create_user(user_data)

# get user by id
@user_router.get("/{id}")
def get_user_by_id(id:int):
    return UserServices.get_user_by_id(id)

# retrieve all users
@user_router.get("/")
def get_all_users():
    return UserServices.get_all_users()

    