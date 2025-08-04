import asyncio,pytest
from playwright.async_api import Playwright, async_playwright, expect

@pytest.mark.asyncio
async def test_run():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demoqa.com/automation-practice-form",wait_until="domcontentloaded")

        # ---------------------
        assert await page.title() == "DEMOQA"
        await context.close()
        await browser.close()
