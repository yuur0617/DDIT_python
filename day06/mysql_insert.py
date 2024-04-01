import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

sql = """INSERT INTO emp (e_id, e_name, gen, addr) 
            VALUES(%s, %s, %s, %s)"""


curs.execute(sql, ('4','4','4','4'))
conn.commit()

curs.close()
conn.close()