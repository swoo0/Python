import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect (
            host='localhost',
            port=3305,
            user='root',
            password='python',
            db='python',
            charset='utf8'
        );
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        print("--- DB 연결완료 ---")
    
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        print("--- DB 연결해제 ---")
    
    
    
    def myinsert(self, s_code, s_name, price, ymd_hm):
        sql = f"""
        insert into 
            stock(s_code, s_name, price, ymd_hm)
            values('{s_code}', '{s_name}', {price}, '{ymd_hm}')
        """
        cnt = self.curs.execute(sql)
    
        self.conn.commit()
        print("intsert 성공 !")

        return cnt
        

if __name__=="__main__" :
    ds = DaoStock()
    cnt = ds.myinsert(1, 1, 1, 1)
    print("cnt", cnt)

    