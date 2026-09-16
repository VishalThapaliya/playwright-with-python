from pathlib import Path
import json
from playwright.sync_api import Page, expect
import pytest

def get_json_data():
    file_path = Path(__file__).parent / "test_data" / "data.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return [(item['username'], item['password']) for item in data]

@pytest.mark.parametrize("username, password", get_json_data())
def test_data_driven(page: Page, username: str, password: str):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page.locator(".oxd-topbar-header-breadcrumb-module")).to_have_text("Dashboard")
