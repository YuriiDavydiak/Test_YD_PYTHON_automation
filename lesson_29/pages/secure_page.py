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
        try:
            return self.page.locator(self.FLASH_MESSAGE).text_content()
        except:
            return ""

    def logout(self):

        try:
            # Спосіб 1: точний селектор
            self.page.click("a[href='/logout']")
        except:
            try:
                # Спосіб 2: селектор з текстом
                self.page.click("text=Logout")
            except:
                try:
                    self.page.click("a:has-text('Logout')")
                except:
                    pass

        try:
            self.page.wait_for_url("**/login", timeout=5000)
        except:
            self.page.wait_for_load_state('networkidle', timeout=5000)

    def is_logout_button_visible(self):

        try:
            return self.page.locator("a[href='/logout']").count() > 0
        except:
            try:
                return self.page.locator("text=Logout").count() > 0
            except:
                return False

    def get_url(self):
        return self.page.url