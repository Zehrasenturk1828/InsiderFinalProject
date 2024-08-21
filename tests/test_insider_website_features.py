import time
import pytest
from pages.home_page import *
from pages.quality_assurance_page import *
from tests.conftest import *


@pytest.mark.usefixtures("setup")
class TestInsiderWebsiteFeatures:
    def test_insider_website_features(self):
        home_page = HomePage(self.driver)
        home_page.verify_load_page()
        home_page.click_cookies()
        home_page.click_company()
        home_page.click_careers()
        home_page.click_all_teams()
        home_page.check_our_locations()
        home_page.life_at_insider()

        quality_assurance_page = QualityAssurancePage(self.driver)
        quality_assurance_page.click_all_jobs()
        quality_assurance_page.click_filter_by_loc()
        quality_assurance_page.click_option_Istanbul()
        quality_assurance_page.click_department()
        quality_assurance_page.click_qa()
        quality_assurance_page.check_all_job_contains()
        quality_assurance_page.click_view_role_btn()
        assert quality_assurance_page.check_url_of_page() == "APPLY FOR THIS JOB"

        
        