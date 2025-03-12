from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_course():
    response = client.post("/courses", json={"title": "Test Course", "description": "This is a test course description."})
    assert response.status_code == 201
    assert response.json()["data"]["title"] == "Test Course"
    assert response.json()["data"]["description"] == "This is a test course description."

def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_get_course():
    # First, create a course to ensure there is one to get
    create_response = client.post("/courses", json={"title": "Test Course", "description": "This is a test course description."})
    course_id = create_response.json()["data"]["id"]

    # Now, get the course by ID
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == course_id

def test_delete_course():
    # First, create a course to ensure there is one to delete
    create_response = client.post("/courses", json={"title": "Test Course", "description": "This is a test course description."})
    course_id = create_response.json()["data"]["id"]

    # Now, delete the course by ID
    response = client.delete(f"/courses/{course_id}")
    assert response.status_code == 204

    # Verify the course has been deleted
    get_response = client.get(f"/courses/{course_id}")
    assert get_response.status_code == 404