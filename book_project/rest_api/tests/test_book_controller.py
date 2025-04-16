
from fastapi.testclient import TestClient
from rest_api.main import app
from rest_api.controller import book_controller
from rest_api.service import book_service
from rest_api.dto import BookDTO
import os

os.environ["API_KEY"] = "test_api_key"

client = TestClient(app)

def test_get_books():
    response = client.get("/books", headers={"api_key": "test_api_key"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book():
    book = {"title": "Test Book", "author": "Test Author", "country": "Test Country"}
    response = client.post("/books", json=book, headers={"api_key": "test_api_key"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_delete_book():
    response = client.delete("/books/Test Book", headers={"api_key": "test_api_key"})
    assert response.status_code == 200
    assert response.json()["message"] == "Book 'Test Book' deleted successfully"
