from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("/Users/gokul/Personal/Projects/Python/Selenium4ExamplesWithPython/Drivers/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")

logoElement = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Google']")))
print(logoElement.rect)

driver.quit()