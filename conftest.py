import pytest

@pytest.fixture
def page(playwright, request):
    headed = request.config.getoption("--headed")
    slow_mo = int(request.config.getoption("--slowmo") or 0)

    browser = playwright.chromium.launch(
        headless = not headed,
        slow_mo = slow_mo
    )

    page = browser.new_page()
    yield page

    page.close()
    browser.close()

