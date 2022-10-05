from selenium import webdriver

driver = webdriver.Firefox(executable_path="/Users/gokul/Personal/Projects/Python/Selenium4ExamplesWithPython/Drivers/geckodriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")

driver.quit()