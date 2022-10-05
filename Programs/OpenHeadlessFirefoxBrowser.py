from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, executable_path='/Users/gokul/Personal/Projects/Python/Selenium4ExamplesWithPython/Drivers/geckodriver')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")

driver.quit()