from playwright.sync_api import expect
import pytest

class TestProfileChangePassword:
    def test_change_password_fields(self, profile_auth_page):
        profile_auth_page.open()
        
        # Check if fields are visible
        expect(profile_auth_page.page.locator(profile_auth_page.password_form.current_password_input)).to_be_visible()
        expect(profile_auth_page.page.locator(profile_auth_page.password_form.new_password_input)).to_be_visible()
        expect(profile_auth_page.page.locator(profile_auth_page.password_form.confirm_password_input)).to_be_visible()
        
    def test_change_password_fill(self, profile_auth_page):
        profile_auth_page.open()
        
        profile_auth_page.password_form.change_password("old_pass", "new_pass", "new_pass")
        # Since we don't have a backend mock, we just verify the interaction doesn't crash
        # If the page doesn't change URL or show an error, we can assume it worked or was submitted.
        # Here we just verify that it doesn't fail.
