import mysql.connector

class update:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Bhanu@17",
            database="bank"
        )

    def myupdate(self,table_name,column_name,new_value,customer_id):
        cur = self.conn.cursor()
        if table_name=='personaldetails' or table_name=='bankdetails':
            if new_value.isnumeric():
                cur.execute(f"UPDATE {table_name} SET {column_name}={new_value} WHERE CID={customer_id}")
            else:
                cur.execute(f"UPDATE {table_name} SET {column_name}='{new_value}' WHERE CID={customer_id}")
            self.conn.commit()
        if table_name=='transactiondetails' or table_name=='accountdetails':
            if new_value.isnumeric():
                cur.execute(f"UPDATE {table_name} SET {column_name}={new_value} WHERE TRANSACTIONID IN(SELECT TRANSACTIONID FROM ACCOUNTDETAILS WHERE ACCOUNT_NUMBER IN(SELECT ACCOUNT_NUMBER FROM BANKDETAILS WHERE CID={customer_id}));")
            else:
                cur.execute(f"UPDATE {table_name} SET {column_name}='{new_value}' WHERE TRANSACTIONID IN(SELECT TRANSACTIONID FROM ACCOUNTDETAILS WHERE ACCOUNT_NUMBER IN(SELECT ACCOUNT_NUMBER FROM BANKDETAILS WHERE CID={customer_id}));")
            self.conn.commit()
        print("Updated successfully")