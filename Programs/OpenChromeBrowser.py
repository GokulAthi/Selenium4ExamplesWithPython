from selenium import webdriver

driver = webdriver.Chrome("/Users/gokul/Personal/Projects/Python/Selenium4ExamplesWithPython/Drivers/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")

driver.quit()