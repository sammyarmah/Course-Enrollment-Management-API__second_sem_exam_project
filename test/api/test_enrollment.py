def test_enroll_student_user(client, student_user):
    response = client.post(
        "/enrollments/",
        json = {
            "user_id": student_user["id"],
            "course_id": 1
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == student_user["id"]
    assert data["course_id"] == 1


def test_enroll_student(client, student_user):
    response = client.post(
        "/enrollments/",
        json = {
            "user_id": student_user["id"],
            "course_id": 1
        }
    )
    enroll_id = response.json()["id"]

    get_response = client.get(f"/enrollments/{enroll_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["user_id"] == student_user["id"]


def test_deregister_student(client, student_user):
    response = client.post(
        "/enrollments/",
        json = {
            "user_id": student_user["id"],
            "course_id": 1
        }
    )
    enrollment_id = response.json()["id"]
    get_response = client.delete(f"/enrollments/{enrollment_id}")
    assert get_response.status_code == 200

def test_admin_to_view_enrollments(client, admin_user):
    response = client.get("/enrollments/")
    assert response.status_code == 200

def test_admin_can_force_deregistration(client, admin_user, student_user):
    response = client.post(
        "/enrollments/",
        json = {
            "user_id": student_user["id"],
            "course_id": 1
        }
    )
    enrollment_id = response.json()["id"]

    deregister = client.delete(f"/enrollments/{enrollment_id}/2")
    assert deregister.status_code == 200



