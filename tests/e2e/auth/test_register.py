import pytest
from playwright.sync_api import expect
from config.config import BASE_URL
from data.register_data import NEGATIVE_REGISTER_CASES
from utils.data_factory import RegistrationFactory


class TestRegister:
    # добавить набор тестовых данных для проверки edge-кейсов
    # проверить использую параметризацию
    def test_register_positive(self, register_page):
        user = RegistrationFactory.create_registration()
        register_page.register(user["email"], user["password"], user["confirm_password"])
        expect(register_page.page).to_have_url(f"{BASE_URL}/")

    @pytest.mark.parametrize(
        "case",
        NEGATIVE_REGISTER_CASES,
        ids=[case["title"] for case in NEGATIVE_REGISTER_CASES]
    )
    def test_register_negative(self, register_page, case):
        register_page.register(case["email"], case["password"], case["confirm_password"])
        error = register_page.get_error()
        assert case["error_message"] in error
