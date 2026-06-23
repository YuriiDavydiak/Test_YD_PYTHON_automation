def test_secure_page_heading(secure_page):
    assert "Secure Area" in secure_page.get_heading_text()


def test_logout_redirects_to_login(secure_page):
    secure_page.logout()
    assert secure_page.page.url.endswith("/login")


def test_logout_shows_flash_message(secure_page):
    secure_page.logout()
    flash_text = secure_page.page.locator("#flash").text_content()
    assert "logged out" in flash_text.lower()

def test_login_page_title(login_page):
    assert login_page.page.title() == "The Internet"


def test_logout_button_disappears_after_logout(secure_page):
    secure_page.logout()
    assert secure_page.page.locator("a[href='/logout']").count() == 0


def test_direct_access_to_secure_without_login_redirects(page):
    page.goto("https://the-internet.herokuapp.com/secure")
    assert page.url.endswith("/login")
    flash_text = page.locator("#flash").text_content()
    assert "must login" in flash_text.lower()