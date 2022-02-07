import pymysql

def dbconnect():
    conn = pymysql.connect (
        host='localhost',
        port=3305,
        user='root',
        password='python',
        db='python',
        charset='utf8'
    );
    return conn

def search_data(conn):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from emp';
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    
    curs.close()
    # for data in rows:
    #     print(data)
        
def insert_data(conn):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    e_id = 7
    e_name = 7
    sex = 7
    age = 7
    sql = f"""insert into `emp`(e_id, e_name, sex, age)
                        values ('{e_id}','{e_name}','{sex}','{age}')"""
    cnt = curs.execute(sql)

    print("cnt", cnt)
    # data = [
    #     {'e_id': '4', 'e_name': '4', 'sex': '4', 'age': 4},
    #     {'e_id': '5', 'e_name': '5', 'sex': '5', 'age': 5},
    #     {'e_id': '6', 'e_name': '6', 'sex': '6', 'age': 6}
    # ]
    # sql = "insert into `emp` values(%(e_id)s, %(e_name)s, %(sex)s, %(age)s);"
    # curs.executemany(sql, data)
    
    
    conn.commit()
    print("intsert 성공 !")
    
    
def update_data(conn):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    e_id = 6
    e_name = 7
    sex = 7
    age = 7
    sql = f"""
            update emp
            set e_name = '{e_name}',
                sex = '{sex}',
                age = {age}
            where e_id = '{e_id}'
        """
    cnt = curs.execute(sql)

    print("cnt", cnt)
    
    conn.commit()
    print("update 성공 !")

def main():        
    conn = dbconnect()
    print('연결완료')
    update_data(conn)
    conn.close()
    print('연결해제')
    
if __name__=="__main__" :
    main()