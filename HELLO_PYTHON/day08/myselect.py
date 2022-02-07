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
    curs = conn.cursor()
    sql = 'select * from emp';
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    
    curs.close()
    # for data in rows:
    #     print(data)
        
def main():        
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결해제')
    
if __name__=="__main__" :
    main()