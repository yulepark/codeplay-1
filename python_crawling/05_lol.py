import time # ?초 기다리기를 위한 모듈
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())
def lol_find(nickname):
    time.sleep(3)
    url = f"https://www.op.gg/summoners/kr/{nickname}"
    browser.get(url)
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source, "lxml")
    name = soup.find("strong", attrs = {"class" : "css-ao94tw e1swkqyq1"})
    rank = soup.find("div", attrs = {"class" : "tier"})
    kda = soup.find("div", attrs = {"class" : "k-d-a"})

    #print("----------실시간 인기 웹툰 5---------")
    print(name.text, rank.text, kda.text)
nick = input("닉네임 입력 : ")
lol_find(nick)

