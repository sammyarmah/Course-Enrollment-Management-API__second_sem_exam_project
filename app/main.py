from fastapi import FastAPI
from app.api.v1.user import user_router
from app.api.v1.course import course_router


app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["Users"])
app.include_router(course_router, prefix="/courses", tags=["Courses"])

