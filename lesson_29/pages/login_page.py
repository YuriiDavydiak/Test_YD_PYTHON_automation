class LoginPage:
    URL = "/login"
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BTN = 'button[type="submit"]'
    FLASH_MESSAGE = "#flash"

    def __init__(self, page):
        self.page = page

    def open(self, base_url):
        self.page.goto(base_url + self.URL)

    def login(self, username, password):
        # Use JavaScript to fill inputs
        self.page.evaluate(f"""
            document.querySelector('{self.USERNAME_INPUT}').value = '{username}';
            document.querySelector('{self.PASSWORD_INPUT}').value = '{password}';
        """)

        # Press Enter on password field to submit form
        self.page.press(self.PASSWORD_INPUT, 'Enter')

        # Wait for navigation - check if URL changed to /secure
        try:
            self.page.wait_for_url("**/secure", timeout=5000)
        except:
            # If not redirected, wait for page load
            try:
                self.page.wait_for_load_state('networkidle', timeout=5000)
            except:
                pass

    def get_flash_message(self):
        try:
            return self.page.locator(self.FLASH_MESSAGE).text_content()
        except:
            return ""

    def is_login_form_visible(self):
        return self.page.locator(self.USERNAME_INPUT).is_visible()

    def get_title(self):
        return self.page.title()
