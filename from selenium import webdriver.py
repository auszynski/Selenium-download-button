#import os
#from selenium import webdriver

#os.environ['PATH'] += r"/Users/Artur/Downloads/chromedriver"
#driver = webdriver.Chrome()

from selenium import webdriver
driver = webdriver.Safari()
driver.get('https://demo.borland.com/testsite/download_testpage.php')
my_element = driver.find_element_by_id('downloadButton')
my_element.click()
