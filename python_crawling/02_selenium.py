import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://www.op.gg/champions")

elem = browser.find_element(By.ID, "searchChampion")
elem.send_keys("아리")
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(2)

browser.get("https://www.naver.com")

elem = browser.find_element(By.ID, "query")
elem.send_keys("코드플레이")
time.sleep(1)
elem.send_keys(Keys.ENTER)

# test = browser.find_element(By.CLASS_NAME, "css-cym2o0 e1oulx2j60")

# print(test)

while True:
    if "q" == input("quit?"):
        break
