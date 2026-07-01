class SecurePage:
    SECURE_HEADING = "h2"
    LOGOUT_BTN = "a[href='/logout']"
    FLASH_MESSAGE = "#flash"

    def __init__(self, page):
        self.page = page

    def is_logged_in(self):
        return "/secure" in self.page.url

    def get_heading_text(self):
        return self.page.locator(self.SECURE_HEADING).text_content()

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE).text_content()

    def logout(self):
        self.page.click(self.LOGOUT_BTN)

    def is_logout_button_visible(self):
        return self.page.locator(self.LOGOUT_BTN).count() > 0

    def get_url(self):
        return self.page.url