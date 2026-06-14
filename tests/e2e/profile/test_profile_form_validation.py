import pytest
from playwright.sync_api import expect
from data.profile_data import INVALID_DATA, DATE_DATA, get_valid_data

class TestProfileFormValidation:
    def test_all_fields_required(self, profile_page):
        profile_page.open()

        profile_page.submit()

        expect(profile_page.page.locator(profile_page.form)).to_be_visible()
    
    @pytest.mark.parametrize("scenario", INVALID_DATA, ids=[s["description"] for s in INVALID_DATA])
    def test_invalid_data(self, profile_page, scenario):
        profile_page.open()

        data = {scenario["field"]: scenario["value"]}
        profile_page.fill_form(**data)
        profile_page.submit()

        expect(profile_page.page.locator(profile_page.form)).to_be_visible()

    @pytest.mark.parametrize("date_scenario", DATE_DATA, ids=[s["description"] for s in DATE_DATA])
    def test_date_of_birth_validation(self, profile_page, date_scenario):
        profile_page.open()
        
        profile_page.fill_form(dob=date_scenario["value"])
        profile_page.submit()

        if not date_scenario["valid"]:
            expect(profile_page.page.locator(profile_page.form)).to_be_visible()


    def test_valid_data(self, profile_page):
        profile_page.open()

        data = get_valid_data()
        profile_page.fill_form(**data)
        profile_page.submit()

        expect(profile_page.page.locator(profile_page.form)).to_be_visible()



