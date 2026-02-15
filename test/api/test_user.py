from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# test to create a new user
def test_create_user():
    response = client.post(
        "/user/",
        json= {
            "name": "Samuel Armah",
            "email": "samuel123@gmail.com",
            "role": "student"
        }
    ) 
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Samuel Armah"
    assert data["email"] == "samuel123@gmail.com"
    assert data["role"] == "student" 

# test to create a user with missing name
def test_create_user_without_name():
    response = client.post(
        "/user/",
        json = {
            "email": "samuel123@gmail.com",
            "role": "student"
        }
    )
    assert response.status_code == 422

# test to create user with invalid email
def test_create_user_with_invalid_email():
    response = client.post(
        "/user/",
        json = {
            "name": "Samuel Armah",
            "email": "samuel123",
            "role": "admin"
        }
    )
    assert response.status_code == 422
    

# testing if role is not either student or admin
def test_create_user_with_wrong_role():
    response = client.post(
        "/user/",
        json = {
            "name": "Samuel Armah",
            "email": "samuel123@gmail.com",
            "role": "teacher"
        }
    )
    assert response.status_code == 422

# test to get a user by id
def test_get_user_by_id():
    response = client.post(
        "/user/",
        json = {
            "name": "Samuel Armah",
            "email": "samuel123@gmail.com",
            "role": "admin"
        }
    )
    user_id = response.json()["id"]

    get_response = client.get(f"/user/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["name"] == "Samuel Armah"
    assert data["email"] == "samuel123@gmail.com"
    assert data["role"] == "admin"
