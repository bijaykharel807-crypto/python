from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://animi-tsore.vercel.app/')
driver.save_screenshot('website.png')
driver.quit()