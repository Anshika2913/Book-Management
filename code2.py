import mysql.connector as sql
mydb = sql.connect(host='localhost', database='bookshop', user='root', password='admin',charset='utf8')
if mydb.is_connected:
     c=mydb.cursor()
     print('Connection established')
     
def book():
   while 1:
     print('*'*95)
     print('\t\t\t\t\tBOOK DETAILS')
     print('*'*95)
     print('''
     1 for adding book
     2 for displaying all book records
     3 for display one record
     4 for deleting all bookrecords
     5 for deleting one record
     6 for modification in details  of book
     7 to back to main menu''')
     choice=int(input('enter above key for following functions'))
     if choice==1:
          add()
     elif choice==2:
          displayall()
     elif choice==3:
          display()
     elif choice==4:
          deleteall()
     elif choice==5:
          delete()
     elif choice==6:
          update()
     elif choice==7:
          main()
     else:
          print('Invalid choice : Try again')
# add book details
def add():
    try:
         ans='yes'
         while ans.lower()=='yes':
              print('enter book information....')
              b_id=int(input('enter bookid:'))
              bname=input('enter bookname')
              aname=input('enter author name')
              year=input('enter year of publication')
              price=float(input('enter price'))
              itstype=input('enter its type')
              quantity=int(input('enter its quantity'))
              query="insert into books (b_id,book_name,author_name,year,price,type,quantity) values({},'{}','{}','{}',{},'{}',{})". format(b_id,bname,aname,year,price,itstype,quantity)
              c.execute(query)
              mydb.commit()
              print('record added')
              ans=input('enter yes to add more file')
    except Exception as e :
        print('something went wrong')
        print(e)
# display all bookdetails
def displayall():
     try:
          c.execute('Select * from books')
          details=c.fetchall()
          for i in details:
               print(i)
     except Exception as e :
          print('something went wrong')
          print(e)
# display selected bookdetails
def display():
     try:
          a=input('enter name of book which you want to display')
          c.execute('Select * from books'.format(a))
          x=c.fetchone()
          print(x)
     except Exception as e :
               print('something went wrong')
               print(e)
# delete selected book               
def delete():
     r=input('Enter bookname whose record you want to delete')
     c.execute("delete from books where book_name='{}'".format(r))
     mydb.commit()
     print('Record deleted successfully')
# delete all bookdetails
def deleteall():
     try:
          r=input('do you want to delete all records?(yes/no)')
          if r.lower()=='yes':
               c.execute("delete from books".format(r))
               mydb.commit()
               print('All Records deleted successfully')
     except Exception as e :
               print('something went wrong')
               print(e)

# update quantity/cost   
def update():
     try:
          r=input('Enter bookname whose cost you want to change')
          n=int(input('enter 1 to update quantity/n enter 2 to update cost'))
          if n==1:
               m=int(input('enter  new quantity'))
               c.execute("update books set quantity='{}' where book_name='{}'".format(m,r))
          elif n==2:
               b=int(input('enter  new  cost'))
               c.execute("update books set price='{}' where book_name ='{}'".format(b,r))
          else:
               print('Invalid choice : Try again')  
          mydb.commit()
          print('Record updated successfully')
     except Exception as e :
          print('something went wrong')
          print(e)
     



def cust():
     while 2:
          print('*'*95)
          print('\t\t\t\t\tCUSTOMER DETAILS')
          print('*'*95)            
          print('''
          1 for adding customer details
          2 for displaying all customers record
          3 for display one customer record
          4 for deleting all customers record
          5 for deleting one customer record
          6 for modification in customer details
          7 to back to main menu''')
          choice=int(input('enter above key for following functions'))
          if choice==1:
               custadd()
          elif choice==2:
               custdisplayall()
          elif choice==3:
               custdisplay()
          elif choice==4:
               custdeleteall()
          elif choice==5:
               custdelete()
          elif choice==6:
               custupdate()
          elif choice==7:
               main()
          else:
               print('Invalid choice : Try again') 
# add customer details     
def custadd():
    try:
         ans='yes'
         while ans.lower()=='yes':
              print('enter customer information....')
              cid=int(input('enter cid:'))
              cname=input('enter name')
              book=input('enter name of bookpurchase ')
              price=float(input('enter price'))
              date=input('enter date of purchase')
              author=input('enter authorname')
              contact=input('enter contactno')
              address=input('enter address')
              query="insert into customers (cno,cname,bookpurchase,price,dateofpurchase,authorname,contactno,address) values({},'{}','{}',{},{},'{}','{}','{}')". format(cid,cname,book,price,date,author,contact,address)
              c.execute(query)
              mydb.commit()
              print('record added')
              ans=input('enter yes to add more file') 
    except Exception as e :
          print('something went wrong')
          print(e)
# display all customer details
def custdisplayall():
     try:
          c.execute('Select * from customers')
          details=c.fetchall()
          for i in details:
               print(i)
     except Exception as e :
          print('something went wrong')
          print(e)
# display selected customer details
def custdisplay():
     try:
          a=int(input('enter customerno which you want to display')) 
          c.execute('Select * from customers'.format(a))
          x=c.fetchone()
          print(x)
     except Exception as e :
               print('something went wrong')
               print(e)
# delete selected customer details
def custdelete():
     r=int(input('Enter customerno whose record you want to delete'))
     c.execute("delete from customers where cno ={}".format(r))
     mydb.commit()
     print('Record deleted successfully')
# delete all customer details
def custdeleteall():
     try:
          r=input('do you want to delete all records?(yes/no)')
          if r.lower()=='yes':
               c.execute("delete from customers".format(r))
               mydb.commit()
               print('All Records deleted successfully')
     except Exception as e :
               print('something went wrong')
               print(e)
# update contact number/address
def custupdate():
     try:
          r=int(input('Enter customerno whose details you want to change'))
          n=int(input('enter 1 to update contact number/n enter 2 to update address'))
          if n==1:
               m=int(input('enter  new contact number'))
               c.execute("update customers set contactno='{}' where cno={}".format(m,r))
          elif n==2:
               b=input('enter  new address')
               c.execute("update customers set address='{}' where cno={}".format(b,r))
          else:
               print('Invalid choice : Try again')               
          mydb.commit()
          print('Record updated successfully')
     except Exception as e :
          print('something went wrong')
          print(e)
def main():
     n=int(input('enter 1 for book details\n enter 2 for customer details'))
     if n==1:
          book()
     elif n==2:
          cust()
     else:
           print('Invalid choice : Try again')
main()          
