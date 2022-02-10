import requests
from bs4 import BeautifulSoup
from day12.daostock import DaoStock
import datetime

ds = DaoStock()
date = datetime.datetime.now()
ymd_hm = date.strftime("%y%m%d_%H%M")
mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding="euc-kr"
soup = BeautifulSoup(mysrc.text, 'html.parser')


class StockRecord:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def stock(self):
        sts = soup.select(".st2")
        
        for idx, st2 in enumerate(sts):
            myparent = st2.parent
            tds = myparent.select("td")
            s_name = tds[0].text
            s_code = tds[0].a['title']
            price = tds[1].text.replace(",", "")
            cnt = ds.myinsert(s_code, s_name, price, ymd_hm);
            print(idx, s_code, s_name, price, ymd_hm, cnt);
            
        
if __name__=="__main__" :
    st = StockRecord()
    st.stock()
