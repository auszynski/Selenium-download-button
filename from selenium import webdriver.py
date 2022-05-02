#import os
#from selenium import webdriver

#os.environ['PATH'] += r"/Users/Artur/Downloads/chromedriver"
#driver = webdriver.Chrome()
import time
from selenium import webdriver
driver = webdriver.Safari()
driver.get('https://demo.borland.com/testsite/download_testpage.php') #adres strony, ktora chcemy uruchomic
driver.implicitly_wait(30) #time.sleep(30)- w wypadku opoznien serwera
my_element = driver.find_element_by_id('downloadButton') #wybranie elementu po id podczas "inspekcji" strony
time.sleep(5) #zatrzymanie testu na 5s aby zobaczyc jak uruchamia sie element download
my_element.click() #czynnosc jaka ma wykonac test w zwiazku z wybranym elementem
