from playwright.sync_api import Page, expect

class Home_page:
    def __init__(self, page: Page):
        self.page = page
        self.performance_button = page.get_by_role("link", name="Performance")
        self.dashboard_button = page.get_by_role("link", name="Dashboard")
        self.myinfo_button = page.get_by_role("link", name="My Info")

    def click_performance(self, page: Page):
        self.performance_button.click()
        expect(page.locator(".oxd-topbar-header-breadcrumb-module")).to_have_text("Performance")

    def click_dashboard(self, page: Page):
        self.dashboard_button.click()
        expect(page.locator(".oxd-topbar-header-breadcrumb-module")).to_have_text("Dashboard")

    def click_myinfo(self, page: Page):
        self.myinfo_button.click()
        expect(page.locator(".oxd-topbar-header-breadcrumb-module")).to_have_text("PIM")