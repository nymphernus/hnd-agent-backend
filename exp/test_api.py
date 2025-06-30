import pytest
from httpx import AsyncClient, ASGITransport

from db import app

@pytest.mark.asyncio
async def test_read_books():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/booksold")
        assert response.status_code == 200

        data = response.json()
        assert len(data) >= 2

@pytest.mark.asyncio
async def test_create_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/booksold", json={
            "title": "Nazvanie",
            "author": "Avtor"
        })
        assert response.status_code == 200

        data = response.json()
        assert data == {"success": True, "message": "Книга добавлена"}

