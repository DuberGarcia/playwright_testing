import pytest
from playwright.async_api import  expect

@pytest.mark.asyncio
async def test_title(page):
    assert await page.title() == "DEMOQA"

@pytest.mark.asyncio
async def test_duber(page):
    await page.get_by_role("textbox", name="First Name").click()
    await page.get_by_role("textbox", name="First Name").fill("duber")
    await page.get_by_role("textbox", name="Last Name").click()
    await page.get_by_role("textbox", name="Last Name").fill("garcia")
    await page.get_by_role("textbox", name="name@example.com").click()
    await page.get_by_role("textbox", name="name@example.com").fill("duebr@example.com")
    await page.get_by_text("Male", exact=True).click()
    await page.get_by_role("textbox", name="Mobile Number").click()
    await page.get_by_role("textbox", name="Mobile Number").fill("1234567890")
    await page.get_by_role("button", name="Submit").click()
    await expect(page.locator("tbody")).to_contain_text("duber garcia")
    await expect(page.locator("tbody")).to_contain_text("duebr@example.com")
    await page.get_by_role("dialog", name="Thanks for submitting the form").click()
    await expect(page.locator("tbody")).to_contain_text("1234567890")
