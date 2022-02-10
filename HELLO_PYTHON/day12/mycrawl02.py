import requests
from bs4 import BeautifulSoup

mysrc = requests.get("http://localhost/emplist")
soup = BeautifulSoup(mysrc.text, 'html.parser')
print(mysrc.text)
print("-----------------------------------------------------------")
# print(soup)

# print(soup.select(".vline")[0].get_text())

mytables = soup.select("table")[0]

trs = mytables.select("tr")

for idx,tr in enumerate(trs):
    if idx > 0:
        td4 = tr.select("td")
        print(td4[0].text,td4[1].text,td4[2].text,td4[3].text)


