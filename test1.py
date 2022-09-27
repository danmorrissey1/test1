from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # Click button:has-text("Log In")
    page.locator("button:has-text(\"Log In\")").click()
    # Click [data-testid="signUp\.switchToSignUp"]
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    # Click [data-testid="siteMembersDialogLayout"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"siteMembersDialogLayout\"] [data-testid=\"buttonElement\"]").click()
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("dan@hotmail.com")
    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("dan123")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
