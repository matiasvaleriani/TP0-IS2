import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
import json

client = TestClient(app)


def test_create_course():
    """
    Tests the course creation endpoint by sending a POST request with sample data.
    Verifies that the response status is 201 and the returned data matches the input.
    """
    response = client.post(
        "/courses",
        json={
            "title": "Test Course",
            "description": "This is a test course description.",
        },
    )
    assert response.status_code == 201
    assert response.json()["data"]["title"] == "Test Course"
    assert (
        response.json()["data"]["description"] == "This is a test course description."
    )

    # Clean up
    course_id = response.json()["data"]["id"]
    delete_response = client.delete(f"/courses/{course_id}")
    assert delete_response.status_code == 204


def test_get_courses():
    """
    Tests the endpoint that retrieves all courses.
    Ensures the response status is 200 and that the returned data is a list.
    """
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)


def test_get_course():
    """
    Tests the retrieval of a specific course by first creating one,
    then requesting it using its ID. Ensures the response status is 200
    and that the returned course ID matches the created one.
    """
    create_response = client.post(
        "/courses",
        json={
            "title": "Test Course",
            "description": "This is a test course description.",
        },
    )
    course_id = create_response.json()["data"]["id"]

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == course_id

    # Clean up
    delete_response = client.delete(f"/courses/{course_id}")
    assert delete_response.status_code == 204


def test_delete_course():
    """
    Tests the course deletion endpoint by creating a course first,
    then deleting it using its ID. Verifies that the response status is 204
    and that attempting to retrieve the deleted course results in a 404 status.
    """
    create_response = client.post(
        "/courses",
        json={
            "title": "Test Course",
            "description": "This is a test course description.",
        },
    )
    course_id = create_response.json()["data"]["id"]

    response = client.delete(f"/courses/{course_id}")
    assert response.status_code == 204

    get_response = client.get(f"/courses/{course_id}")
    assert get_response.status_code == 404
