import pytest
from playwright.sync_api import expect
from config.config import BASE_URL, loginCredentials
from data.login_data import NEGATIVE_LOGIN_CASES


class TestLogin:
    def test_successful_login(self, login_page):
        login_page.login(
            loginCredentials["email"],
            loginCredentials["password"]
        )

        expect(login_page.page).to_have_url(f"{BASE_URL}/")

    @pytest.mark.parametrize(
        "case",
        NEGATIVE_LOGIN_CASES,
        ids=[case["title"] for case in NEGATIVE_LOGIN_CASES]
    )
    def test_negative_login(self, login_page, case):
        login_page.login(case["email"], case["password"])
        error = login_page.get_error()
        assert case["error"] in error
