from fastapi.testclient import TestClient
from app.main import app
from app.api.deps import is_admin_user
from app.api.deps import is_student_user
from app.core.enrollment import enrollment_db
import pytest

@pytest.fixture(autouse=True)
def clear_enrollment_db():
    enrollment_db.clear()


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def admin_user():
    fake_admin_user = {
        "id": 1,
        "role": "admin"
    }
    def admin_user_override(user_id: int = 1):
        return fake_admin_user["id"]
    
    app.dependency_overrides[is_admin_user] = admin_user_override
    yield fake_admin_user
    app.dependency_overrides = {}

@pytest.fixture
def student_user():
    fake_student_user = {
        "id": 2,
        "role": "student"
    }
    def student_user_override(user_id: int = 2):
        return fake_student_user["id"]

    app.dependency_overrides[is_student_user] = student_user_override
    yield fake_student_user
    app.dependency_overrides = {}

