import pytest

@pytest.mark.asyncio
async def test_title(page):
    assert await page.title() == "DEMOQA"

