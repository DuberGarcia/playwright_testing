import pytest
from playwright.async_api import async_playwright

@pytest.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True,args=["--no-sandbox", "--disable-setuid-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demoqa.com/automation-practice-form")
        yield page
        await context.close()
        await browser.close()
