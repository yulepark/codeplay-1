import requests
from bs4 import BeautifulSoup
import lxml

cheat = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

url = "https://www.op.gg/champions"   #접속해 훔쳐올 웹사이트 주소


resource = requests.get(url, headers = cheat)
resource.raise_for_status() #제대로 접속되면 진행. 아니면 스탑.

#with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
#    file.write(resource.text)


soup = BeautifulSoup(resource.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])
print(soup.img)
print(soup.img.attrs)
print(soup.img["src"])




print(soup.find("a", attrs = "<a href="/champions/kaisa/adc?region=global&amp;tier=platinum_plus"))
print(soup.find(attrs = "<a href="/champions/kaisa/adc?region=global&amp;tier=platinum_plus"))
print(soup.find("a", attrs = "<a href="/champions/kaisa/adc?region=global&amp;tier=platinum_plus")get_text())


