from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
driver = webdriver.Chrome('c:/selenium/chromedriver')

#driver = webdriver.Chrome()
driver.get('https://www.naver.com/')
time.sleep(1)

# 로그인 버튼을 찾고 클릭합니다
login_btn = driver.find_element_by_class_name('link_login')
login_btn.click()
time.sleep(1)

# id, pw 입력할 곳을 찾습니다.
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy('whdgus1323')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('Name1s-JongHyeon')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('log.login')
login_btn.click()



search_btn.click()
