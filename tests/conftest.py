import pytest
from httpx import AsyncClient

from app.main import fast


@pytest.fixture()
def client() -> AsyncClient:
    return AsyncClient(app=fast, base_url="http://test")
