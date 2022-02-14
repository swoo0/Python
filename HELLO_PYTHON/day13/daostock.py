import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                               db='python',port=3305, charset='utf8')
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor) 
        
    def myselect(self,s_name):
        sql = f"""
        select 
            s_code,
            s_name,
            price,
            ymd_hm
        from 
            stock
        where
            s_name = '{s_name}'
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def myprices(self,s_name):
        ret = []
        sql = f"""
        select 
            s_code,
            s_name,
            price,
            ymd_hm
        from 
            stock
        where
            s_name = '{s_name}'
        order by ymd_hm
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        for p in mylist:
            ret.append(p['price'])
        return ret    
    
    
    def mys_names(self):
        sql = f"""
        select 
            s_name
        from 
            stock
        group by s_name
        # LIMIT 6
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    


    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    a=[]
    b=[]
    # de = DaoStock()
    # mylist = de.mys_names()
    # for n in mylist:
    #     s_name = n['s_name']
    #     prices = de.myprices(s_name)
    #     print(s_name,prices)
    #     a.append(s_name)
    #     b.append(prices)
    #
    # print(a)
    # print(b)

    
    
    
    
    