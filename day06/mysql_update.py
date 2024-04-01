import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

e_id ="6"
e_name ="7"
gen ="7"
addr ="7"

sql = f"""
        UPDATE emp
        SET 
            e_name='{e_name}', gen='{gen}', addr='{addr}'
        WHERE e_id = '{e_id}'
"""
        
cnt = curs.execute(sql)
print(cnt)
# print(curs.rowcount)

conn.commit()

curs.close()
conn.close()