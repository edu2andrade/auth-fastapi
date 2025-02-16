import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.database import engine
from sqlmodel import SQLModel

@pytest.fixture()
def client():
    SQLModel.metadata.create_all(engine)
    yield TestClient(app)
    SQLModel.metadata.drop_all(engine)