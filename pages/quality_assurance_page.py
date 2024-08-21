from asyncio import timeout
import time
import pytest
from pages.constants.homepage_constants import *
from pages.base_page import *
from pages.constants.qualityassurance_constants import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import re

@pytest.mark.usefixtures("setup")
class QualityAssurancePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        BASE_URL = "https://useinsider.com/careers/quality-assurance/"
        driver.get(BASE_URL)

    def click_all_jobs(self):
        all_jobs = self.wait_element_visibility(SEE_ALL_JOBS)
        all_jobs.click()
    
    def click_filter_by_loc(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@title="Quality Assurance"]'))
            )
            print("Page loaded.")
        except Exception:
            print("There was a problem loading the page or the item was not found.")
        location_filter = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(FILTER_BY_LOCATION))
        location_filter.click()

    def click_option_Istanbul(self):
        Istanbul = self.wait_element_visibility(SELECT_LOCATION)
        Istanbul.click()

    def click_department(self):
        department = self.wait_element_visibility(DEPARTMENT)
        department.click()
    
    def click_qa(self):
        quality_assurance = self.wait_element_visibility(SELECT_DEPARTMENT)
        quality_assurance.click()
        time.sleep(10)

    def check_all_job_contains(self):
        try:
            result = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(JOB_TITLE)
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(result).perform()
            print("Page loaded.")
        except Exception:
            print("There was a problem loading the page or the item was not found.")

        all_job_listing = self.find_elements(ALL_JOBS)

        if not all_job_listing:
            raise AssertionError("No job listings found.")

        for job in all_job_listing:
            try:
                print(f"Checking job...")

                position = self.wait_element_presence(JOB_TITLE)
                if position.text.find("Quality Assurance") != -1:
                    print("Position contains 'Quality Assurance'")
                else:
                    raise AssertionError("Position does not contain 'Quality Assurance'")

                department = self.wait_element_presence(JOB_DEPARTMENT)
                if department.text.find("Quality Assurance") != -1:
                    print("Department contains 'Quality Assurance'")
                else:
                    raise AssertionError("Department does not contain 'Quality Assurance'")

                location = self.wait_element_presence(JOB_LOCATION)
                if location.text.find("Istanbul, Turkey") != -1:
                    print("Location contains 'Istanbul, Turkey'")
                else:
                    raise AssertionError("Location does not contain 'Istanbul, Turkey'")
        
            except Exception as e:
                self.driver.save_screenshot("error_job.png")
                raise AssertionError("An error occurred for job")
    
    def click_view_role_btn(self):
        actions = ActionChains(self.driver)
        click_btn = self.get_element_of_index(0, *VIEW_ROLE_BTN)
        actions.move_to_element(click_btn).click().perform()

    def check_url_of_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        find_lever = WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located(APPLY_BTN)
        )
        return find_lever.text
        


