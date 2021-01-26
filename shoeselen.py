from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#Size_input = input("Choose size from 5-12...")

option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\eastbot\chromedriver.exe", options=option)
driver.get('https://www.titan22.com/customer/account/login/')

#login to the account manually

#go to a shoe before pressing enter

input("Press Enter to continue...")


wait = WebDriverWait(driver, 30)

Dropdown_menu = wait.until(EC.presence_of_element_located((By.ID, 'attribute139'))).click()

def Size_5():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="154"]'))).click()

def Size_55():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="155"]'))).click()

def Size_6():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="156"]'))).click()

def Size_65():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="157"]'))).click()

def Size_7():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="158"]'))).click()

def Size_75():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="159"]'))).click()

def Size_8():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="160"]'))).click()

def Size_85():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="161"]'))).click()

def Size_9():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="162"]'))).click()

def Size_95():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="174"]'))).click()

def Size_10():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="163"]'))).click()

def Size_105():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="164"]'))).click()

def Size_11():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="165"]'))).click()

def Size_115():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="166"]'))).click()

def Size_12():
	wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="167"]'))).click()
    

if Size_input == '5':
    Size_5()

elif Size_input =='5.5':
	Size_55()

elif Size_input =='6':
	Size_6()

elif Size_input =='6.5':
	Size_65()

elif Size_input =='7':
	Size_7()

elif Size_input =='7.5':
	Size_75()

elif Size_input =='8':
	Size_8()

elif Size_input =='8.5':
	Size_85()

elif Size_input =='9':
	Size_9()

elif Size_input =='9.5':
	Size_95()

elif Size_input =='10':
	Size_10()

elif Size_input =='10.5':
	Size_105()

elif Size_input =='11':
	Size_11()

elif Size_input =='11.5':
	Size_115()

elif Size_input =='12':
	Size_12()

Quantity = 1 
qtty = driver.find_element_by_id('qty')
qtty.send_keys(Quantity)

add_to_cart = driver.find_element_by_id("product-addtocart-button").click()

check_out = wait.until(EC.presence_of_element_located((By.ID, 'ajaxcart_checkout'))).click()

print("Sleeping for 5 seconds")
time.sleep(5)

paypal = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'braintree_paypal'))).click()

driver.switch_to.frame(2)

time.sleep(2)
print(driver.page_source)
driver.find_element_by_class_name("paypal-button-logo").click()