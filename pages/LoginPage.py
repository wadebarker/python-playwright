from pages.BasePage import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):

    parent = ".Login_content__AK6sN"

    email_input = f"{parent} input[type='email']"
    password_input = f"{parent} input[type='password']"
    submit_button = f"{parent} button[type='submit']"
    error_block = f"{parent} .text-red-500"

    def open(self):
        self.goto(f"{BASE_URL}/auth/login")

    def login(self, email, password):
        self.open()
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.submit_button)

    def get_error(self):
        return self.page.locator(self.error_block).inner_text()
