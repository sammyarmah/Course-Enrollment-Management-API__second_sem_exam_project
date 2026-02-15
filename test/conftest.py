from fastapi.testclient import TestClient
from app.main import app
from app.api.deps import is_admin_user
from app.api.deps import is_student_user
import pytest


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def admin_user():
    def admin_user_override():
        return 1
    
    app.dependency_overrides[is_admin_user] = admin_user_override
    yield
    app.dependency_overrides = {}

@pytest.fixture
def student_user():
    def student_user_override():
        return 1

    app.dependency_overrides[is_student_user] = student_user_override
    yield
    app.dependency_overrides = {}

