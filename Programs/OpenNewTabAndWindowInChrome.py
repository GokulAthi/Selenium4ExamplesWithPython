from selenium import webdriver

driver = webdriver.Chrome("/Users/gokul/Personal/Projects/Python/Selenium4ExamplesWithPython/Drivers/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")
print("Page title -> "+driver.title)

driver.switch_to.new_window('tab')
driver.get("https://simplytechnified.com/find-elements-with-relative-locator-strategy-using-selenium-4-and-java/")
print("Page title of new tab -> "+driver.title)

driver.switch_to.new_window('window')
driver.get("https://simplytechnified.com/read-server-client-logcat-logs-using-appium-and-java/")
print("Page title of new window -> "+driver.title)

driver.quit()