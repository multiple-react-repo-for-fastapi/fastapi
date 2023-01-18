import pytest

from app.core.models import User


pytestmark = [pytest.mark.django_db, pytest.mark.asyncio]


async def test_get_hello_view(client):
    """Tests whether the view can use a Django model"""
    old_count = await User.objects.acount()
    assert old_count == 0
    async with client as ac:
        response = await ac.get("/hello")
    assert response.status_code == 200
    new_count = await User.objects.acount()
    assert new_count == 1
    assert response.json() == {"message": "Hello World, count: 1"}


async def test_clears_database_after_test(client):
    """Testing whether Django clears the database"""
    await test_get_hello_view(client)
