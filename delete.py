import mysql.connector

class delete:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Bhanu@17",
            database="bank"
        )

    def data_delete(self,table_name,customer_id):
        cur = self.conn.cursor()
        if table_name=='personaldetails' or table_name=='bankdetails':
            cur.execute(f"DELETE FROM {table_name} WHERE CID ={customer_id};")
            self.conn.commit()
        
