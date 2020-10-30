#Kinesys Facebook Auto Login.py
import time
from myid import ID, PW
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.facebook.com')

time.sleep(3) #대기시간(3)

#로그인 구문 
login_id = driver.find_element_by_name('user id')
login_id.send_keys(ID)
login_pw = driver.find_element_by_name('user pw')
login_pw.send_keys(PW)
login_pw_send_keys(Keys.RETURN)

time.sleep(3)
