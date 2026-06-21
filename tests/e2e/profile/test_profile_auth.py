from config import config
from pages.profile.ProfileAuthPage import ProfileAuthPage


class TestProfileAuth:
    # Проверка открытия страницы и отображения элементов на ней
    def test_auth_tab_opens_after_login(self, profile_auth_page):
        expected_url = config.BASE_URL + "/profile/authorization"
        page_url = profile_auth_page.page.url
        assert page_url == expected_url, f"Expected URL to be {expected_url}, got {page_url}"

        assert profile_auth_page.is_visible(ProfileAuthPage.EMAIL_CONTAINER), "Секция 'Почта' должна быть видима"
        assert profile_auth_page.is_visible(ProfileAuthPage.PASSWORD_CONTAINER), "Секция 'Смена пароля' должна быть видима"


    # проверка отображения элементов формы смены почты
    def test_email_section_contains_all_fields(self, profile_auth_page):
        assert profile_auth_page.is_visible(ProfileAuthPage.EMAIL_INPUT), "Поле ввода почты должно быть видимо"
        assert profile_auth_page.is_visible(
            ProfileAuthPage.EMAIL_PASSWORD_INPUT), "Поле подтверждения пароля для почты должно быть видимо"
        assert profile_auth_page.is_visible(ProfileAuthPage.EMAIL_SAVE_BUTTON), "Кнопка сохранения почты должна быть видима"



    # проверка отображения элементов формы смены пароля
    def test_change_password_section_contains_all_fields(self, profile_auth_page):
        assert profile_auth_page.is_visible(ProfileAuthPage.CURRENT_PASSWORD_INPUT), "Поле текущего пароля должно быть видимо"
        assert profile_auth_page.is_visible(ProfileAuthPage.NEW_PASSWORD_INPUT), "Поле нового пароля должно быть видимо"
        assert profile_auth_page.is_visible(
            ProfileAuthPage.CHECK_NEW_PASSWORD_INPUT), "Поле повторного пароля должно быть видимо"
        assert profile_auth_page.is_visible(ProfileAuthPage.PASSWORD_SAVE_BUTTON), "Кнопка сохранения пароля должна быть видима"


    # тест на проверку смены почты
    def test_successful_email_update_dom_level(self, profile_auth_page):
        test_email = "vadim_zviagintsev555@mail.ru"
        confirm_password = "Qwerty123"

        profile_auth_page.set_email(test_email)
        profile_auth_page.set_email_password(confirm_password)
        profile_auth_page.submit_email_form()

        profile_auth_page.open()

        email_value = profile_auth_page.get_input_value(ProfileAuthPage.EMAIL_INPUT)
        email_pass_value = profile_auth_page.get_input_value(ProfileAuthPage.EMAIL_PASSWORD_INPUT)

        assert email_value == test_email, "Ожидалось сохранённое значение email в поле"
        assert email_pass_value == confirm_password, "Ожидалось значение в поле подтверждения пароля для почты"