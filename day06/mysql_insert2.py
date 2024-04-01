import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

e_id ="6"
e_name ="6"
gen ="6"
addr ="6"

sql = f"""
        INSERT INTO emp (e_id, e_name, gen, addr) 
            VALUES('{e_id}', '{e_name}', '{gen}', '{addr}')
"""
        
cnt = curs.execute(sql)
print(cnt)
# print(curs.rowcount)

conn.commit()

curs.close()
conn.close()