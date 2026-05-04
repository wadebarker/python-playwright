from pages.BasePage import BasePage


class HeaderComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.search_input = ".Header_search-input__d5jfb"
        self.main_page_link = "a[href='/']"
        self.profile_link = "a[href='/profile']"
        self.logout_button = ".Header_logout__vw_E5"

    def search(self, text):
        self.page.locator(self.search_input).fill(text)

    def open_main_page(self):
        self.page.locator(self.main_page_link).click()

    def open_profile(self):
        self.page.locator(self.profile_link).click()

    def logout(self):
        self.page.locator(self.logout_button).click()
