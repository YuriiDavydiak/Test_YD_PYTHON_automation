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
        username_input = self.page.locator(self.USERNAME_INPUT)
        password_input = self.page.locator(self.PASSWORD_INPUT)
        submit_btn = self.page.locator(self.SUBMIT_BTN)

        username_input.click()
        username_input.clear()
        username_input.type(username)

        password_input.click()
        password_input.clear()
        password_input.type(password)

        submit_btn.click()

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE).text_content()

    def is_login_form_visible(self):
        return self.page.locator(self.USERNAME_INPUT).is_visible()

    def get_title(self):
        return self.page.title()