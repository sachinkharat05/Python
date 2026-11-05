from playwright.sync_api import sync_playwright


def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto("https://example.com")

        assert page.title() == "Example Domain"

        heading = page.locator("h1")
        assert heading.inner_text() == "Example Domain"

        browser.close()
