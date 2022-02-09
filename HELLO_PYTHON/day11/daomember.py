import pymysql

class DaoMember:
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
        self.curs.close();
        self.conn.close();
        print("--- DB 연결해제 ---")
    
    
    def myselect(self):    
        sql = f"""
        select m_id,
               m_name,
               tel,
               addr
          from 
               member
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    def myinsert(self, m_name, tel, addr):
        sql = f"""
        insert into
            member(m_name, tel, addr)
            values({m_name}, {tel}, {addr})
        """
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        print("insert 성공")
        
        return cnt
        
    def myupdate(self, m_id, m_name, tel, addr):
        sql = f"""
        update member
        set m_name = {m_name},
            tel = {tel},
            addr = {addr}
        where m_id = {m_id}
        """
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        print("update 성공 !")
        
        return cnt
        
    def mydelete(self, m_id):
        sql = f"""
        delete from member
        where m_id = {m_id}
        """
        cnt = self.curs.execute(sql)
        
        if cnt == 1 :
            self.conn.commit()
            print("delete 성공 !")
    
        return cnt
    
    
if __name__=='__main__':
    dm = DaoMember()
    # mylist = de.myselect()
    # print(mylist)
    # cnt = de.myinsert(4, 4, 4)
    # print(cnt)
    # cnt = de.myupdate(5, 5, 5, 5)
    # print(cnt)
    # cnt = de.mydelete(5)
    # print(cnt)