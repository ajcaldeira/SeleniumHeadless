import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = r'C:\Users\theni\AppData\Local\Google\Chrome SxS\Application\chrome.exe'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"), chrome_options=chrome_options)  
driver.get("http://www.duo.com")

magnifying_glass = driver.find_element_by_xpath('//*[@id="js-navbar__nav"]/div/span/p/a[2]')
security = driver.find_element_by_css_selector('h2')
print("Found: " + security.text)

driver.close()