import pymysql

class DaoEmp:
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
    
    
    def myselect(self):
        sql = f"""
        select e_id,
               e_name,
               sex,
               age
          from 
               emp
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        return mylist
    
    
    def myinsert(self, e_name, sex, age):
        sql = f"""
        insert into 
            emp(e_name, sex, age)
            values({e_name}, {sex}, {age})
        """
        cnt = self.curs.execute(sql)
    
        self.conn.commit()
        print("intsert 성공 !")

        return cnt
        
        
    def myupdate(self, e_id, e_name, sex, age):
        sql = f"""
        update emp
        set e_name = {e_name}, 
            sex = {sex},
            age = {age}
        where e_id = {e_id}
        """
        cnt = self.curs.execute(sql) 
        
        self.conn.commit()
        print("update 성공 !")
        
        return cnt
    
    
    def mydelete(self, e_id):
        sql = f"""
        delete from emp
         where e_id = {e_id}
        """
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        print("delete 성공 !")
        
        return cnt


if __name__=="__main__" :
    de = DaoEmp()
    # mylist = de.myselect()
    # print(mylist)
    # cnt = de.myinsert(9, 9, 9)
    # print("cnt", cnt)
    # cnt = de.myupdate(13, 7, 7, 7)
    # print("cnt", cnt)
    cnt = de.mydelete(13)
    print("cnt", cnt)
    