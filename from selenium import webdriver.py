#import os
#from selenium import webdriver

#os.environ['PATH'] += r"/Users/Artur/Downloads/chromedriver"
#driver = webdriver.Chrome()

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.google.pl/index.html")