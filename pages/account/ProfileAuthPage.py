from pages.BasePage import BasePage
from config.config import BASE_URL
from components.profile.ChangeEmailComponent import ChangeEmailComponent
from components.profile.ChangePasswordComponent import ChangePasswordComponent


class ProfileAuthPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.email_form = ChangeEmailComponent(self.page)
        self.password_form = ChangePasswordComponent(self.page)

    def open(self):
        self.goto(f"{BASE_URL}/profile/authorization")
