from selenium.webdriver.common.by import By

SEE_ALL_JOBS = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")
FILTER_BY_LOCATION = (By.CSS_SELECTOR, "span#select2-filter-by-location-container")
SELECT_LOCATION = (By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
DEPARTMENT = (By.ID, "select2-filter-by-department-container")
SELECT_DEPARTMENT = (By.XPATH, "/html/body/span/span/span[2]/ul/li[15]")
POSITION_RESULTS = (By.XPATH, "//*[@id='career-position-list']/div/div/div[1]/h3")
ALL_JOBS = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div")
JOB_TITLE = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > p")
JOB_DEPARTMENT = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > span")
JOB_LOCATION = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > div")
HOVER_ON_JOBS = (By.XPATH, "//*[@id='jobs-list']/div[1]")
VIEW_ROLE_BTN = (By.CSS_SELECTOR, "a[class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5']")
APPLY_BTN = (By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/a")