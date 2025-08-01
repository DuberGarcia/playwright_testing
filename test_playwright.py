import re
import pytest
from playwright.async_api import async_playwright,expect

@pytest.mark.asyncio
async def test_run() -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width":1920,"height":1080})
        page = await context.new_page()
        await page.goto("https://demoqa.com/automation-practice-form",wait_until="load")
        await page.get_by_role("textbox", name="First Name").fill("duber")
        await page.get_by_role("textbox", name="First Name").press("Tab")
        await page.get_by_role("textbox", name="Last Name").fill("garcia")
        await page.get_by_role("textbox", name="name@example.com").fill("duber.example@emzapmle.com")
        await page.locator("div").filter(has_text=re.compile(r"^Male$")).click()
        await page.get_by_text("Male", exact=True).click()
        await page.get_by_role("textbox", name="Mobile Number").fill("1234567891")
        await page.get_by_text("Reading").click()
        await page.get_by_role("button", name="Submit").click()
        await expect(page.locator("thead")).to_contain_text("Values")
        await expect(page.locator("tbody")).to_contain_text("duber garcia")
        await expect(page.locator("tbody")).to_contain_text("duber.example@emzapmle.com")
        await expect(page.locator("tbody")).to_contain_text("Male")
        await expect(page.locator("tbody")).to_contain_text("1234567891")
        await expect(page.locator("tbody")).to_contain_text("Reading")
        await page.screenshot(path="captura_post_toolsQA.png")
        await page.get_by_role("button", name="Close").click()

        await context.close()

        await browser.close()

@pytest.mark.asyncio
async def test_api_success():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        response = await request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        await request_context.disp