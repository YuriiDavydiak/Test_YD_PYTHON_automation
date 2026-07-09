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
        # Fill username field
        self.page.fill(self.USERNAME_INPUT, username)

        self.page.fill(self.PASSWORD_INPUT, password)

        self.page.press(self.PASSWORD_INPUT, 'Enter')

        try:
            self.page.wait_for_url("**/secure", timeout=5000)
        except:
            self.page.wait_for_load_state('networkidle', timeout=5000)

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE).text_content()

    def is_login_form_visible(self):
        return self.page.locator(self.USERNAME_INPUT).is_visible()

    def get_title(self):
        return self.page.title()
