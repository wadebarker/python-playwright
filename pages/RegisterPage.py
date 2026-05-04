from pages.BasePage import BasePage
from config.config import BASE_URL


class RegisterPage(BasePage):

    parent = ".Register_content__MmAGw"

    email_input = f"{parent} input[type='email']"
    password_input = f"{parent} #register-pass"
    confirm_password_input = f"{parent} #register-pass-two"
    submit_button = f"{parent} button[type='submit']"
    error_block = f"{parent} .text-red-500"

    def open(self):
        self.goto(f"{BASE_URL}/auth/register")

    def register(self, email, password, confirm_password):
        self.open()
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.fill(self.confirm_password_input, confirm_password)
        self.click(self.submit_button)

    def get_error(self):
        return self.page.locator(self.error_block).inner_text()