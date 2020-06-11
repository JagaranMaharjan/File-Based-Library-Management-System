#readDisplayRetunHistory is a function which donot have any parameter and return type value
#this module is to display the return book history of a program
def readDisplayRetunHistory():
   print('============================================================Book Returned History Of Library==========================================================')
   print('======================================================================================================================================================')
   print('SN.\tBook-ID\t\tName\t\tDate\t\t\tBook Name\t\t\tStock\t\tReturned\tUpdated Stock Quantity')
   print('======================================================================================================================================================')
   file = open('History_Multiple_Of_Book_Return.txt','r')
   key = 1
   for line in file:
       print(' ', key, '\t'+ line.replace(',','\t\t'))
       key = key + 1
       print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
   print('=======================================================================================================================================================')
