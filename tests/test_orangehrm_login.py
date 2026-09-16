from playwright.sync_api import Page
from pages.orangehrm_login_page import Login_page
from pages.organehrm_home_page import Home_page

def test_oragehrm_login(page: Page):
    login_page = Login_page(page)
    home_page = Home_page(page)

    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login_page.login('Admin', 'admin123')

    home_page.click_myinfo(page)
    home_page.click_performance(page)
    home_page.click_dashboard(page)
