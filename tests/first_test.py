import re
from playwright.sync_api import Page, expect
url = "https://playwright.dev/"

def test_playwright_homepage(page: Page):
    page.goto(url)

    expect(page).to_have_title(re.compile("Playwright"))
    print("Page title: ", page.title())

def test_get_started_link(page: Page):
    page.goto(url)

    page.get_by_role("link", name = "Get started").click()

    expect(page.get_by_role("heading", name = "Installation")).to_be_visible()