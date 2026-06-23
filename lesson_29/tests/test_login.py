import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("LOGIN_PASSWORD")


def test_successful_login(secure_page):
    assert secure_page.is_logged_in()
    assert "secure area" in secure_page.get_heading_text().lower()


def test_login_with_wrong_password(login_page):
    login_page.login(USERNAME, "wrong_password")
    assert "invalid" in login_page.get_flash_message().lower()


def test_login_with_wrong_username(login_page):
    login_page.login("wrong_user", PASSWORD)
    assert "invalid" in login_page.get_flash_message().lower()


def test_login_with_empty_fields(login_page):
    login_page.login("", "")
    assert login_page.is_login_form_visible()