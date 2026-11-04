
from playwright.sync_api import sync_playwright

def test_login(base_url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(base_url)

        page.locator('input[name="username"]').nth(0).fill(
            "Sachin"
        )
        page.locator('input[name="email"]').fill(
            "sachin@gmail.com"
        )
        page.locator('input[name="password"]').nth(0).fill(
            "Sachin123"
        )
        page.get_by_role("button", name="Register").click()
        assert page.get_by_text(
            "Registration Successful"
        ).is_visible()

        # Enter username
        page.locator('input[name="username"]').nth(1).fill(
            "Sachin"
        )

        # Enter password
        page.locator('input[name="password"]').nth(1).fill(
            "Sachin123"
        )

        # Click Login button
        page.get_by_role("button", name="Login").click()

        # Verify login
        assert page.get_by_text(
            "Login Successful"
        ).is_visible()

        print("Login Test Passed")

        browser.close()
