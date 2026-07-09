import pytest


@pytest.mark.secure_area
class TestSecureArea:

    @pytest.mark.regression
    def test_logout_redirects_to_login(self, secure_page):
        secure_page.logout()
        assert secure_page.get_url().endswith("/login")

    @pytest.mark.smoke
    def test_login_page_title(self, login_page):
        assert login_page.get_title() == "The Internet"

    @pytest.mark.regression
    def test_logout_button_disappears_after_logout(self, secure_page):
        secure_page.logout()
        assert secure_page.is_logout_button_visible() is False

    @pytest.mark.regression
    def test_direct_access_to_secure_without_login_redirects(self, page):
        page.goto("https://the-internet.herokuapp.com/secure")
        from pages.login_page import LoginPage
        lp = LoginPage(page)
        assert page.url.endswith("/login")
        assert "must login" in lp.get_flash_message().lower()