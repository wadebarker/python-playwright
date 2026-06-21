from playwright.sync_api import Page, expect
from typing import Optional
from pages import BasePage


class ProfileAuthPage(BasePage):
    NAV = ".NavLine_nav__JR5gH"
    PERSONAL_INFO_TAB = NAV + " a[href='/profile']"
    AUTHORIZATION_TAB = NAV + " a[href='/profile/authorization']"
    ACTIVE_TAB = NAV + " .NavLine_active__w2KGW"

    # Parent/containers
    PARENT = ".Authorization_wrapper__vtNRF"
    CONTAINER = PARENT + " .Authorization_container__gFYDn"

    # "Почта" — first container
    EMAIL_CONTAINER = CONTAINER + ":nth-of-type(1)"
    EMAIL_SECTION = EMAIL_CONTAINER + " h2"
    EMAIL_INPUT = EMAIL_CONTAINER + " input[name='email']"
    EMAIL_PASSWORD_INPUT = EMAIL_CONTAINER + " input#pass-id-email"
    EMAIL_SAVE_BUTTON = EMAIL_CONTAINER + " button[type='button'], " + EMAIL_CONTAINER + " button"

    # "Смена пароля" — second container
    PASSWORD_CONTAINER = CONTAINER + ":nth-of-type(2)"
    CHANGE_PASSWORD_SECTION = PASSWORD_CONTAINER + " h2"
    CURRENT_PASSWORD_INPUT = PASSWORD_CONTAINER + " input[name='password']"
    NEW_PASSWORD_INPUT = PASSWORD_CONTAINER + " input[name='newpass']"
    CHECK_NEW_PASSWORD_INPUT = PASSWORD_CONTAINER + " input[name='checkNewPass']"
    PASSWORD_SAVE_BUTTON = PASSWORD_CONTAINER + " button[type='button'], " + PASSWORD_CONTAINER + " button"

    def __init__(self, page: Page, base_url: Optional[str] = None):
        super().__init__(page)
        self.page: Page = page
        self.base_url = base_url

    def get_url(self) -> str:
        return self.base_url + "/profile/authorization"

    def open(self) -> None:
        self.page.goto(self.get_url())

    # методы для смены почты
    def set_email(self, email: str) -> None:
        self.page.locator(self.EMAIL_INPUT).wait_for(state="visible", timeout=10000)
        self.page.fill(self.EMAIL_INPUT, email)

    def set_email_password(self, password: str) -> None:
        self.page.locator(self.EMAIL_PASSWORD_INPUT).wait_for(state="visible", timeout=10000)
        self.page.fill(self.EMAIL_PASSWORD_INPUT, password)

    def submit_email_form(self) -> None:
        self.page.locator(self.EMAIL_SAVE_BUTTON).wait_for(state="visible", timeout=10000)
        self.page.click(self.EMAIL_SAVE_BUTTON)


    # методы для смены пароля
    def set_current_password(self, password: str) -> None:
        self.page.locator(self.CURRENT_PASSWORD_INPUT).wait_for(state="visible", timeout=10000)
        self.page.fill(self.CURRENT_PASSWORD_INPUT, password)

    def set_new_password(self, password: str) -> None:
        self.page.locator(self.NEW_PASSWORD_INPUT).wait_for(state="visible", timeout=10000)
        self.page.fill(self.NEW_PASSWORD_INPUT, password)

    def set_check_new_password(self, password: str) -> None:
        self.page.locator(self.CHECK_NEW_PASSWORD_INPUT).wait_for(state="visible", timeout=10000)
        self.page.fill(self.CHECK_NEW_PASSWORD_INPUT, password)

    def submit_password_form(self) -> None:
        self.page.locator(self.PASSWORD_SAVE_BUTTON).wait_for(state="visible", timeout=10000)
        self.page.click(self.PASSWORD_SAVE_BUTTON)

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible()
        except Exception:
            return False
