class LoginPage:
    URL = "/login"
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BTN = "button[type='submit']"
    FLASH_MESSAGE = "#flash"

    def __init__(self, page):
        self.page = page

    def open(self, base_url):
        self.page.goto(base_url + self.URL)

    def login(self, username, password):
        # Use JavaScript to fill inputs, bypassing Playwright API issues
        self.page.evaluate(f"""
            document.querySelector('{self.USERNAME_INPUT}').value = '{username}';
            document.querySelector('{self.PASSWORD_INPUT}').value = '{password}';
        """)
        self.page.click(self.SUBMIT_BTN)

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE).text_content()

    def is_login_form_visible(self):
        return self.page.locator(self.USERNAME_INPUT).is_visible()

    def get_title(self):
        return self.page.title()