from pages.BasePage import BasePage


class HeaderComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.search_input = ".Header_search-input__d5jfb"
        self.main_page_link = "a[href='/']"
        self.profile_link = "a[href='/profile']"
        self.logout_button = ".Header_logout__vw_E5"
        self.header_container = ".Header_header__YBrvA"

    def wait_for_header(self, timeout=5000):
        self.page.locator(self.header_container).wait_for(state="visible", timeout=timeout)
        return self

    def search(self, text, wait_for_results=False):
        search_locator = self.page.locator(self.search_input)
        search_locator.wait_for(state="visible")
        search_locator.fill(text)
        if wait_for_results:
            self.page.wait_for_load_state("networkidle")
        return self

    def get_search_value(self):
        return self.page.locator(self.search_input).input_value()

    def clear_search(self):
        self.page.locator(self.search_input).fill("")
        return self

    def open_main_page(self):
        self.page.locator(self.main_page_link).click()
        # "networkidle" - означает отсутствие сетевых запросов минимум 500 миллисекунд
        self.page.wait_for_load_state("networkidle")
        return self

    def open_profile(self):
        self.page.locator(self.profile_link).click()
        self.page.wait_for_load_state("networkidle")
        return self

    def logout(self):
        self.page.locator(self.logout_button).click()
        self.page.wait_for_load_state("networkidle")
        return self
