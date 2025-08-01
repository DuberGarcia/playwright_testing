import re
import pytest
from playwright.async_api import async_playwright,expect

@pytest.mark.asyncio
async def test_api_success():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        await request_context.dis