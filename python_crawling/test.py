import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.op.gg/summoners/kr/misals')
source = BeautifulSoup(site.text, 'html.parser')
character = source.select('.css-1pirsze e17e77tq9 .vm-placement' )

for title in issue:
    print(title.get_text())


