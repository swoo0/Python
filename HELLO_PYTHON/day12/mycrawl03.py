import requests
from bs4 import BeautifulSoup

mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding="euc-kr"
soup = BeautifulSoup(mysrc.text, 'html.parser')
# print(mysrc.text)
print("-----------------------------------------------------------")
# print(soup)

sts = soup.select(".st2")

for idx, st2 in enumerate(sts):
    myparent = st2.parent
    tds = myparent.select("td")
    s_name = tds[0].text
    s_code = tds[0].a['title']
    price = tds[1].text
    
    print(idx+1,s_name, s_code, price)

print("-----------------------------------------------------------")
