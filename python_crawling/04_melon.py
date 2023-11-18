import time # ?초 기다리기를 위한 모듈
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.melon.com/chart/index.htm"

browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")
top100 = soup.find("div", attrs = {"class" : "service_list_song type02 d_song_list"})

song = top100.findAll("div", attrs = {"class" : "ellipsis rank01"})
artist = top100.findAll("div", attrs = {"class" : "ellipsis rank02"})
album = top100.findAll("div", attrs = {"class" : "ellipsis rank03"})
like = top100.findAll("button", attrs = {"class" : "button_etc like"})

#print("----------실시간 인기 웹툰 5---------")
for i in range(5):
    ac = len(artist[i].text) // 2
    a = song[i].text.strip('\n')
    b = artist[i].text[ac:].strip('\n')
    c = album[i].text.strip('\n')
    d = like[i].text[9:].strip('\n')
    print(f"{i+1} - {a} - {b} - {c} - {d}")

urls = ["https://www.melon.com/chart/day/index.htm", "https://www.melon.com/chart/week/index.htm", "https://www.melon.com/chart/month/index.htm"]
titles