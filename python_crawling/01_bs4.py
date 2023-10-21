import requests
from bs4 import BeautifulSoup
import lxml

url = ""
cheat = {"accept=language" : "ko_KR", "User-agent" : "Mozilla/5.8(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()

soup = BeautifulSoup