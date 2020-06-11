#readDisplayBorrowedHistory is function which donot have a parameter and return type value
#this is a module that is used to display the borrowed history of a program
def readDisplayBorrowedHistory():
   print('===============================================================History Book Borrowed in Library================================================================')
   print('===============================================================================================================================================================')
   print('SN.\t\tName\t\tDate\t\t\tBook-ID\t\tStock\t\tOrdered\t\tUpdated\t\tPrice')
   print('===============================================================================================================================================================')
   file = open('History_Of_Borrowing_Book_In_Library.txt','r')
   key = 1
   for line in file:
       print(' ', key, '\t\t'+ line.replace(',','\t\t'))
       key = key + 1
       print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')
   print('================================================================================================================================================================')
