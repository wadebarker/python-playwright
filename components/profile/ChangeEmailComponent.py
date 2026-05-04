from pages.BasePage import BasePage


class ChangeEmailComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.parent = ".Authorization_container__gFYDn >> nth=0"  # первый блок на странице

        # Поля
        self.email_input = f"{self.parent} input[name='email']"
        self.password_input = f"{self.parent} input[name='password']"
        self.save_button = f"{self.parent} button"

    def change_email(self, new_email, password):
        self.page.locator(self.email_input).fill(new_email)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.save_button).click()
