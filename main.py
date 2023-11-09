from create import insert
from read import read
from update import update
from delete import delete


obj=insert()
obj1=read()
obj2=update()
obj3=delete()

print("--------- Bank Management System ---------")
print("For Inserting the data enter 1")
print("For Reading the data enter 2")
print("For Updating the data enter 3")
print("For Deleting the data enter 4")

opr = int(input("Please enter your operation: "))

def myopr():
    print("----- For Personal details enter 1 --------")
    print("----- For Bank details enter 2 ------------")
    print("----- For Transaction details enter 3 -----")
    print("----- For Account details enter 4 ---------")
    vr = int(input("Please select your table : "))

    if vr == 1:
        return 'personaldetails'
    elif vr == 2:
        return 'bankdetails'
    elif vr == 3:
        return 'transactiondetails'
    elif vr == 4:
        return 'accountdetails'


if opr == 1:
    h = myopr()
    if h=='personaldetails':
        cid = int(input("Please enter customer id: "))
        fname = input("Please enter customer first name: ")
        lname = input("Please enter customer last name: ")
        addr = input("Please enter customer address: ")
        pn = int(input("Please enter customer phone number: "))
        an = int(input("Please enter customer aadhar number: "))
        pan = input("Please enter customer pan number: ")

        obj.personaldetails(cid,fname,lname,addr,pn,an,pan)

    elif h=='bankdetails':
        acn = int(input("Please enter account number: "))
        cid = int(input("Please enter customerid: "))
        ifsc = input("Please enter ifsc code: ")
        actype = input("Please enter account type: ")

        obj.bankdetails(acn,cid,ifsc,actype)

    elif h=='transactiondetails':
        tid = int(input("Please enter transaction id: "))
        s_ac = int(input("Please enter sender account number: "))
        r_ac = int(input("Please enter receiver account number: "))
        amt = int(input("Please enter amount: "))
        method = input("Please enter method: ")

        obj.transactiondetails(tid,s_ac,r_ac,amt,method)
    
    elif h=='accountdetails':
        acn = int(input("Please enter account number: "))
        tid = int(input("Please enter transaction id: "))
        amt = int(input("Please enter amount: "))
        c_bal = int(input("Please enter closing balance: "))
        tntype = input("Please enter transaction type: ")

        obj.accountdetails(acn,tid,amt,c_bal,tntype)


if opr == 2:
    i = myopr()
    custid = int(input("Please enter customer id for fetching data: "))
    obj1.specific_info(custid,i)


if opr == 3:
    j = myopr()
    colname = input("Please enter column name: ")
    newval = input("Please enter new value: ")
    custid = int(input("Please enter customer id for fetching data: "))
    obj2.myupdate(j,colname,newval,custid)

if opr == 4:
    k = myopr()
    custid = int(input("Please enter customer id: "))
    obj3.data_delete(k,custid)