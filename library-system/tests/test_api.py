from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_root_redirect_to_docs():
    response = client.get("/", follow_redirects=False)
    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/docs"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "Library Management System"


def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) > 0


def test_get_book_by_isbn():
    response = client.get("/books/978-0132350884")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Clean Code"


def test_get_book_not_found():
    response = client.get("/books/000-0000000000")
    assert response.status_code == 404


def test_list_members():
    response = client.get("/members")
    assert response.status_code == 200
    members = response.json()
    assert isinstance(members, list)
    assert any(m["member_id"] == "MEM-001" for m in members)


def test_get_member():
    response = client.get("/members/MEM-001")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice Smith"


def test_return_book_not_found():
    response = client.post("/loans/return", json={"loan_id": "LN-NONEXISTENT"})
    assert response.status_code == 400
    assert "not found" in response.json()["detail"]
