# Generate Playwright code with recording
# execute 'playwright codegen <URL location>' command on terminal
# It will open a browser and will record all the steps we perform and generate code as per our steps performed

# Example: Go to "saucedemo.com", login, add items to cart, remove item from cart, checkout

import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_saucedemo_checkout(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()

    page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"checkout\"]").click()

    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Bishal")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("Thapaliya")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("38000")

    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()

    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")