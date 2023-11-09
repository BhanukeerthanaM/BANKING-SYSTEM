import mysql.connector

class read:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Bhanu@17",
            database="bank"
        )

    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name=='personaldetails' or table_name=='bankdetails':
            cur.execute(f"SELECT * FROM {table_name} WHERE CID={customer_id};")
            print(cur.fetchall())
        if table_name=='transactiondetails' or table_name=='accountdetails':
            cur.execute(f"SELECT * FROM {table_name} WHERE TRANSACTIONID IN(SELECT TRANSACTIONID FROM ACCOUNTDETAILS WHERE ACCOUNT_NUMBER IN(SELECT ACCOUNT_NUMBER FROM BANKDETAILS WHERE CID={customer_id}));")
            print(cur.fetchall())
