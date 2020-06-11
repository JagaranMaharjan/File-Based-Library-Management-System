#importing build in package
import datetime
#importing the local package
import Module_1_Read_Display_File
import Module_2_DictionaryBookData
# dicFile is a variable that assign the value of Module_2_DictionaryBookData
dicFile = Module_2_DictionaryBookData.dictionaryFileList()
#transaction is a function which donot conatin a parameter and no return type value
def transaction():
    value1 = False
    while value1 == False:
        #try and except is used to be safe from program crash
        # in this program if user input any string character instead of number then except will handel the program by displaying some message
        try:
            print('Press key :')
            print('1 to borrow book')
            print('2 to return book')
            print('3 to show return history')
            print('4 to show borrowed history')
            print('Press any number to exit')
            num = int(input('Enter a key :'))
            if num == 1:
                print('1 to borrow book')
                import Module_3_1_Borrowing_Part_Of_Transaction
                Module_3_1_Borrowing_Part_Of_Transaction.borrowing()
                value1 = True
            elif num == 2:
                print('2 to return book')
                import Module_3_2_Returning_Part_Of_Transaction
                Module_3_2_Returning_Part_Of_Transaction.bookReturn()
                value1 = True
            elif num == 3:
                import Module_3_3_History_Of_Returning_Book_In_Library
                Module_3_3_History_Of_Returning_Book_In_Library.readDisplayRetunHistory()
            elif num == 4:
                import Module_3_4_History_Of_Borrowed_Book_In_Library
                Module_3_4_History_Of_Borrowed_Book_In_Library.readDisplayBorrowedHistory()  
            else:
                # value1 = True it means if num is not equal to 1, 2, 3, 4 then it will break down the while loop
                print('Thank your for giving your precious time to our libary.')
                value1 = True
        except:
            print('The key that you have entered is invalid.')
            print()
