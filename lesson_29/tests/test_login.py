import os
import pytest
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("LOGIN_PASSWORD")


@pytest.mark.login
class TestLogin:

    @pytest.mark.regression
    def test_login_with_wrong_password(self, login_page):
        login_page.login(USERNAME, "wrong_password")
        assert "invalid" in login_page.get_flash_message().lower()

    @pytest.mark.regression
    def test_login_with_wrong_username(self, login_page):
        login_page.login("wrong_user", PASSWORD)
        assert "invalid" in login_page.get_flash_message().lower()

    @pytest.mark.regression
    def test_login_with_empty_fields(self, login_page):
        login_page.login("", "")
        assert login_page.is_login_form_visible()
