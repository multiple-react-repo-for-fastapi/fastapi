import pytest
from httpx import AsyncClient

from app.main import fast


@pytest.fixture(autouse=True)
def _cleanup_database():
    """
    The database isn't cleaned up properly due to the client hitting the FastAPI
    endpoints without terminating the transaction.
    """
    # TODO database clean up not working


@pytest.fixture()
def client() -> AsyncClient:
    return AsyncClient(app=fast, base_url="http://test")
