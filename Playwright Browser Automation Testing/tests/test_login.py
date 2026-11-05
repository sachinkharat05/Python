from playwright.sync_api import Page, expect


def test_valid_credentials(page: Page):
    page.goto("http://localhost:8000/login")

    page.get_by_label("Username").fill("valid_student")
    page.get_by_label("Password").fill("valid_test_password")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("http://localhost:8000/dashboard")
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


def test_invalid_password(page: Page):
    page.goto("http://localhost:8000/login")

    page.get_by_label("Username").fill("valid_student")
    page.get_by_label("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")
    expect(page).to_have_url("http://localhost:8000/login")


def test_empty_input_fields(page: Page):
    page.goto("http://localhost:8000/login")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()

    # Verify application-specific required-field validation or native HTML validation.


def test_protected_page_after_logout(page: Page):
    page.goto("http://localhost:8000/login")

    page.get_by_label("Username").fill("valid_student")
    page.get_by_label("Password").fill("valid_test_password")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("http://localhost:8000/dashboard")

    page.get_by_role("button", name="Logout").click()
    page.goto("http://localhost:8000/dashboard")

    expect(page).to_have_url("http://localhost:8000/login")
