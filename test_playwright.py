import pytest

@pytest.mark.asyncio
async def test_run(page):
    await page.goto("https://demoqa.com/automation-practice-form")
    assert await page.title() == "DEMOQA"

