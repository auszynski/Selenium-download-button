
#import os
#from selenium import webdriver

#os.environ['PATH'] += r"/Users/Artur/Downloads/chromedriver"
#driver = webdriver.Chrome()
import time
from pkg_resources import find_distributions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('https://jqueryui.com/resources/demos/progressbar/download.html') #adres strony, ktora chcemy uruchomic
driver.implicitly_wait(30) #time.sleep(30)- w wypadku opoznien serwera
#my_element = driver.find_element_by_id('downloadButton')
my_element = driver.find_element(By.ID,'downloadButton') #to samo co wyzej
time.sleep(3) #zatrzymanie testu na 3s aby zobaczyc jak uruchamia sie element download
my_element.click() #czynnosc jaka ma wykonac test w zwiazku z wybranym elementem

#progress_element = driver.find_element_by_class_name('progress-label')
#print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label') ,
        'Complete!' #oczekiwany tekst
    )
)   #linie 25-29 pozwalaja na usuniecie lini 22-23. program bedzie dalej dzialal