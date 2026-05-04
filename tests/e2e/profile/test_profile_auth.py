from config.config import BASE_URL
from playwright.sync_api import expect


class TestProfileAuthorization:
    def test_profile_forms_visible(self, profile_auth_page):
        assert profile_auth_page.email_form.is_visible(profile_auth_page.email_form.email_input)
        assert profile_auth_page.email_form.is_visible(profile_auth_page.email_form.password_input)
        assert profile_auth_page.password_form.is_visible(profile_auth_page.password_form.current_password_input)
        assert profile_auth_page.password_form.is_visible(profile_auth_page.password_form.new_password_input)
        assert profile_auth_page.password_form.is_visible(profile_auth_page.password_form.confirm_password_input)

    def test_open_profile_from_dashboard_header(self, dashboard_page):
        dashboard_page.header.open_profile()
        expect(dashboard_page.page).to_have_url(f"{BASE_URL}/profile")
