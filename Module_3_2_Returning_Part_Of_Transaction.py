#this module is used to return book, to create the return book history and charge fine if the book are not return in time
#importing the build in package
import datetime
#importing local package
import Module_1_Read_Display_File
import Module_2_DictionaryBookData
import Module_3_Main_Transaction_Part
#storing the value of module 2 in a varianle called dicFile
dicFile = Module_2_DictionaryBookData.dictionaryFileList()
def bookReturn():
    bookValues = False
    while bookValues == False:
        #try is used to run the error free code
        #except is used to handle the error of a program by displaying some message
        #if user input a key as a string then except will handle the program by displaying some message
        try:
            print('Do you want to return more than one book ?')
            print('If yes then press 1 to return more than one book at a time, 0 to return a book and press any number to exit')
            num = int(input('Press 1 to return more than one book at a time, 0 to return a book and press any number to exit :'))
            if num == 0:
                returnName = input('Enter your name :')
                a = 0
                while a <= num:
                    # a is a append mode that is used to add text in afile without replacing any old values.
                    returnFile = open('History_Multiple_Of_Book_Return.txt','a')
                    a = a + 1
                    keysValue = False
                    while keysValue == False:
                        try:
                            print('Choose a Book-ID from 1 to 10')
                            key1 = int(input('Enter the Book-ID that you want to return to our library :'))
                            file5 = open('stock.txt','r')
                            if key1 > 0 and key1 < 11:
                                #generating date and time from user
                                year = datetime.datetime.now().year
                                month = datetime.datetime.now().month
                                day = datetime.datetime.now().day
                                print(year,'-',month,'-',day)
                                daysValue = False
                                while daysValue == False:
                                    try:
                                        todaysDay = int(input('Enter the day when you have borrowed the book :'))
                                        if todaysDay>0 and todaysDay<=int(day) and todaysDay<31:
                                            daysValue = True
                                        else:
                                            print('The day that you have entered is invalid')
                                            daysValue = False                                            
                                    except:
                                        print('The day that you have entered is in invalid format')
                                        print('Enter the valid day from 1 to '+str(day))
                                bookFine = 5
                                cd = 0
                                fine2 = 0
                                if todaysDay<int(day):
                                    cd = int(day)-todaysDay
                                    if cd < 10:
                                        print('Thank you for your punctuality.')
                                    else:
                                        de = int(day)-(todaysDay+10)
                                        #print(de)
                                        fine2 = de*bookFine
                                total = fine2
                                print('Total Fine you have to pay is : Rs',total)
                                #str is a keyword that is used to convert interger or float number into string
                                returnFile.write(str(key1)+',')
                                returnFile.write(str(returnName) + ',')
                                returnFile.write(str(year)+'-'+str(month)+'-'+str(day)+',')
                                clientValue = False
                                while clientValue == False:
                                    try:
                                        clientQuantity = int(input('What quantity of book do you want to return to our libary ?\n'))
                                        for key, value2 in dicFile.items():
                                            if key1 == key:
                                                if clientQuantity > 0 :
                                                    count = 0
                                                    for j in range(len(value2)):
                                                        if j == count:
                                                            bookName = value2[j]
                                                            returnFile.write(str(bookName)+',')
                                                            print('Book Name :',bookName)
                                                            count1 = count + 1
                                                        elif j == count1:
                                                            authorName = value2[j]
                                                            print('Author Name :',authorName)
                                                            count2 = count1 + 1
                                                        elif j==count2:
                                                            quantity = value2[j]
                                                            print('Quantity :',quantity)
                                                            updatedQuantity = quantity+clientQuantity
                                                            returnFile.write(str(quantity) +',')
                                                            returnFile.write(str(clientQuantity) +',')
                                                            returnFile.write(str(updatedQuantity) +'\n')
                                                            print('Updated Quantity',updatedQuantity)
                                                            value2[j]=updatedQuantity
                                                            count3 = count2 + 1
                                                        elif j==count3:
                                                            price = value2[j]
                                                            print('Price($) :',price)
                                                            returnFile.close()
                                                            clientValue = True
                                                        else:
                                                            print('Index out of bound')  
                                                else:
                                                    print('The qunatity of book that you have entered in our libary is insufficient.')
                                                    print()
                                                    clientValue = False
                                    except:            
                                        print('Please enter the valid quantity in a number')
                                keysValue = True
                            else:
                                print('The Book-ID that you have entered is invalid. Please enter the valid Book-ID in a number between 1 to 10.')
                                print()
                        except:
                            print('The Book-ID that you have entered is invalid. Please enter the valid Book-ID in a number between 1 to 10.')
                            print()
            elif num == 1:
                returnName = input('Enter your name :')
                a = 0
                while a <= num:
                    returnFile = open('History_Multiple_Of_Book_Return.txt','a')
                    a = a + 1
                    keysValue = False
                    while keysValue == False:
                        try:
                            print('Choose a Book-ID from 1 to 10')
                            key1 = int(input('Enter the Book-ID that you want to return to our library :'))
                            file5 = open('stock.txt','r')
                            if key1 > 0 and key1 < 11:
                                year = datetime.datetime.now().year
                                month = datetime.datetime.now().month
                                day = datetime.datetime.now().day
                                print(year,'-',month,'-',day)
                                daysValue = False
                                while daysValue == False:
                                    try:
                                        todaysDay = int(input('Enter the day when you have borrowed the book :'))
                                        if todaysDay>0 and todaysDay<=int(day) and todaysDay<31:
                                            daysValue = True
                                        else:
                                            print('The day that you have entered is invalid')
                                            daysValue = False                                            
                                    except:
                                        print('The day that you have entered is in invalid format')
                                        print('Enter the valid day from 1 to '+str(day))
                                bookFine = 5
                                cd = 0
                                fine2 = 0
                                if todaysDay<int(day):
                                    cd = int(day)-todaysDay
                                    if cd < 10:
                                        print('Thank you for your punctuality.')
                                    else:
                                        de = int(day) - (todaysDay + 10)
                                        fine2 = de*bookFine
                                total = fine2
                                print('Total Fine you have to pay is : Rs',total)
                                returnFile.write(str(key1)+',')
                                returnFile.write(str(returnName) + ',')
                                returnFile.write(str(year)+'-'+str(month)+'-'+str(day)+',')
                                clientValue = False
                                while clientValue == False:
                                    try:
                                        clientQuantity = int(input('What quantity of book do you want to return to our libary ?\n'))
                                        for key, value2 in dicFile.items():
                                            if key1 == key:
                                                if clientQuantity > 0 :
                                                    count = 0
                                                    for j in range(len(value2)):
                                                        if j == count:
                                                            bookName = value2[j]
                                                            returnFile.write(str(bookName)+',')
                                                            print('Book Name :',bookName)
                                                            count1 = count + 1
                                                        elif j == count1:
                                                            authorName = value2[j]
                                                            print('Author Name :',authorName)
                                                            count2 = count1 + 1
                                                        elif j==count2:
                                                            quantity = value2[j]
                                                            print('Quantity :',quantity)
                                                            updatedQuantity = quantity+clientQuantity
                                                            returnFile.write(str(quantity) +',')
                                                            returnFile.write(str(clientQuantity) +',')
                                                            returnFile.write(str(updatedQuantity) +'\n')
                                                            print('Updated Quantity',updatedQuantity)
                                                            value2[j]=updatedQuantity
                                                            count3 = count2 + 1
                                                        elif j==count3:
                                                            price = value2[j]
                                                            print('Price($) :',price)
                                                            returnFile.close()
                                                            clientValue = True
                                                        else:
                                                            print('Index out of bound')  
                                                else:
                                                    print('The qunatity of book that you have entered in our libary is insufficient.')
                                                    print()
                                                    clientValue = False
                                    except:            
                                        print('Please enter the valid quantity in a number')
                                keysValue = True
                            else:
                                print('The Book-ID that you have entered is invalid. Please enter the valid Book-ID in a number between 1 to 10.')
                                print()
                        except:
                            print('The Book-ID that you have entered is invalid. Please enter the valid Book-ID in a number between 1 to 10.')
                            print()     
            else:
                break
        except: 
            print('The key that you have entered is invalid')
            print()
    #w is a write mode that is used to write in file by replacing the old text
    fileUpdate = open('stock.txt','w')
    for value3 in dicFile.values():
        for m in range(len(value3)):
            x = str(value3[m])
            if m!=3:
                fileUpdate.write(x + ',')
            else:
                fileUpdate.write('$' + x + '\n')
    fileUpdate.close()
    Module_1_Read_Display_File.readDisplayFile()
    Module_3_Main_Transaction_Part.transaction()
