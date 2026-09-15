import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(request):
    headed = request.config.getoption("--headed")
    slow_mo = request.config.getoption("--slowmo")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed, slow_mo=slow_mo)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()