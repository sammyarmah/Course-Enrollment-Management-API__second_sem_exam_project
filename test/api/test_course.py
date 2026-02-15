# test to create a course as an admin
def test_create_course(client, admin_user):
    response = client.post(
        "/courses/",
        json = {
            "title": "Business Administration",
            "code": "BA234"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Business Administration"
    assert data["code"] == "BA234"

# test to confirm only admin can update course
def test_admin_can_update_course(client, admin_user):
    response = client.post(
        "/courses/",
        json = {
            "title": "Business Administration",
            "code": "BA234"
        }
    )
    course_id = response.json()["id"]

    update_course = client.put(
        f"/courses/{course_id}",
        json = {
            "title": "Computer Science",
            "code": "CS993"
        }
    )
    assert update_course.status_code == 200

# test when title is missing
def test_create_course_without_title(client, admin_user):
    response = client.post(
        "/courses/",
        json = {
            "code": "BA234"
        }
    )
    assert response.status_code == 422

# test to get course by id
def test_get_course_by_id(client, admin_user):
    response = client.post(
        "/courses/",
        json = {
            "title": "Business Administration",
            "code": "BA234"
        }
    )
    course_id = response.json()["id"]

    get_response = client.get(f"/courses/{course_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["title"] == "Business Administration"
    assert data["code"] == "BA234"

# test for admin to delete
def test_delete_course_by_admin(client, admin_user):
    response = client.delete("/courses/1")
    assert response.status_code == 200

