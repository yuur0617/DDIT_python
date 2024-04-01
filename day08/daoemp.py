import pymysql

class DaoEmp:  
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = 'SELECT * FROM emp'
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def select(self,e_id):
        sql = f"""
            SELECT * FROM emp
            WHERE 
                e_id='{e_id}'
        """
        self.curs.execute(sql)
        list = self.curs.fetchone()
        return list
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
            INSERT INTO 
                emp (e_id, e_name, gen, addr) 
            VALUES
                ('{e_id}', '{e_name}', '{gen}', '{addr}') 
        """
        cnt = self.curs.execute(sql)    
        self.conn.commit()
        return cnt

    def update(self, e_id, e_name, gen, addr):
        sql = f"""
            UPDATE emp
            SET 
                e_name='{e_name}', gen='{gen}', addr='{addr}'
            WHERE 
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp
            WHERE 
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # list = de.selectList()
    # vo = de.select("2")
    # cnt = de.insert('6','6','6','6')
    # cnt = de.update('6', '7', '7', '7')
    cnt = de.delete('6')
    print(cnt)