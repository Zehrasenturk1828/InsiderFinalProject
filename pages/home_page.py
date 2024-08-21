import pytest
from pages.constants.homepage_constants import *
from pages.base_page import *
from selenium.webdriver import ActionChains 

@pytest.mark.usefixtures("setup")

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def verify_load_page(self):
        assert self.get_URL() == "https://useinsider.com/"

    def click_cookies(self):
        cookies_button = self.wait_element_visibility(COOKIES)
        cookies_button.click()
        
    def click_company(self):
        navbar_company = self.wait_element_visibility(COMPANY)
        navbar_company.click()
    
    def click_careers(self):
        dropdown_career = self.wait_element_visibility(CAREERS)
        dropdown_career.click()

    def click_all_teams(self):
        all_teams = self.wait_element_visibility(ALL_TEAMS)
        actions = ActionChains(self.driver)
        actions.move_to_element(all_teams).perform()
        all_teams.click()
    
    def check_our_locations(self):
        our_locations = self.wait_element_presence(OUR_LOCATIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(our_locations).perform()

    def life_at_insider(self):
        life_at_insider = self.wait_element_presence(LIFE_AT_INSIDER)
        actions = ActionChains(self.driver)
        actions.move_to_element(life_at_insider).perform()