from fastapi.testclient import TestClient

from src.app.main import app
from src.models.user import User

client = TestClient(app)


def test_create_user():
    user = User(username="Zohar", email="zohar123@gmail.com", password="123!")
    response = client.post("/users", json=user.model_dump())
    print(f"{response=}")
