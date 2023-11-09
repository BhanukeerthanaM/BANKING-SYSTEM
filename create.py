import mysql.connector

#creating connection

class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Bhanu@17",
            database="bank"
        )
    def personaldetails(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONALDETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},{an},'{pan}')")
        self.conn.commit()
        print("Personal information has been saved successfully.")

    def bankdetails(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO BANKDETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("Bank details have been saved successfully.")

    def transactiondetails(self,tid,s_ac,r_ac,amt,method):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTIONDETAILS VALUES({tid},{s_ac},{r_ac},{amt},'{method}')")
        self.conn.commit()
        print("Transaction details have been saved successfully.")

    def accountdetails(self,acn,tid,amt,c_bal,tntype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNTDETAILS VALUES({acn},{tid},{amt},{c_bal},'{tntype}')")
        self.conn.commit()
        print("Account details have been saved successfully.")
