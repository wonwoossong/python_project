from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser= webdriver.Chrome("./chromedriver_exe")

#네이버로 이동
browser.get("http://naver.com")

#로그인 버튼 클릭 
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

# 아이디와 패스워드 입력

browser.find_element(By.ID,"id").send_keys("nvar")
browser.find_element(By.ID,"pw").send_keys("123123")

#로그인 버튼 클릭
browser.find_element(By.ID,"log.login").click()
time.sleep(3)

#id 새로 입력 
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("dbdn96")
browser.find_element(By.ID,"pw").send_keys("Thddnjsdn123!")
browser.find_element(By.ID,"log.login").click()


# html 정보출력
print(browser.page_source)

#브라우저 종료
browser.quit()

#마음대로종료 안되게  
while(True):
    pass