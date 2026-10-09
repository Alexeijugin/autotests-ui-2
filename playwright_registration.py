from playwright.sync_api import expect, sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    page.get_by_test_id("registration-form-email-input").locator("input").fill("user.name@gmail.com")
    page.get_by_test_id("registration-form-username-input").locator("input").fill("username")
    page.get_by_test_id("registration-form-password-input").locator("input").fill("password")


    page.get_by_test_id("registration-page-registration-button").click()


    dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text("Dashboard")



