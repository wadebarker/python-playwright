from pages.BasePage import BasePage


class ChangePasswordComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.parent = ".Authorization_container__gFYDn >> nth=1"  # второй блок на странице

        self.current_password_input = f"{self.parent} input[name='password']"
        self.new_password_input = f"{self.parent} input[name='newpass']"
        self.confirm_password_input = f"{self.parent} input[name='checkNewPass']"
        self.save_button = f"{self.parent} button"

    def change_password(self, current_password, new_password, confirm_password):
        self.page.locator(self.current_password_input).fill(current_password)
        self.page.locator(self.new_password_input).fill(new_password)
        self.page.locator(self.confirm_password_input).fill(confirm_password)
        self.page.locator(self.save_button).click()
