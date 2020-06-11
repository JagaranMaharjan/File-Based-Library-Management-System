#this module is used for borrowing book, to create the borrowed book history and to generate the acccurate invoice
#importing the build in package
import datetime
#importing local package
import Module_1_Read_Display_File
import Module_2_DictionaryBookData
#storing the value of module 2 in a varianle called dicFile
dicFile = Module_2_DictionaryBookData.dictionaryFileList()
import Module_3_Main_Transaction_Part
def borrowing():
    billList = []
    borrowerName = input('Enter your name :')
    removeSpace = borrowerName.replace(' ','')
    lowerCaseName = removeSpace.lower()
    #date = datetime.datetime.now()
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    billFile = open(lowerCaseName+'.txt','a')
    # a is a append mode that is used to add text in afile without replacing any old values.
    historyFile = open('History_Of_Borrowing_Book_In_Library.txt','a')
    billFile.write('Client Name :'+ str(borrowerName) + '\n')
    billFile.write('Transaction Date :'+str(date)+'\n')
    billFile.write('===================='+'\n')
    bookValues = False
    while bookValues == False:
        try:
            #try is used to run the error free code
            #except is used to handle the error of a program by displaying some message
            #if user input a key as a string then except will handle the program by displaying some message  
            print('Do you want to buy more than one book ?')
            print('If yes then press 1 to buy more than one book at a time, 0 to buy a book and press any number to exist')
            num = int(input('Enter 1 to buy more than one book at a time, 0 to buy a book and press any number to exist :'))
            if num == 0:
                a = 0
                while a <= num:
                    a = a + 1
                    #historyFile.write(borrowerName+',')
                    #historyFile.write(str(date)+',')
                    keysValue = False
                    while keysValue == False:
                        try:
                            print('Choose a Book-ID from 1 to 10')
                            key1 = int(input('Enter the Book-ID that you want to borrow :'))
                            file5 = open('stock.txt','r')
                            if key1 > 0 and key1 < 11:
                                #historyFile.write(str(key1)+',')
                                clientValue = False
                                while clientValue == False:
                                    try:
                                        clientQuantity = int(input('What quantity of book do you want to borrow from our libary ?\n'))
                                        for key, value2 in dicFile.items():
                                            if key1 == key:
                                                if clientQuantity > 0 and clientQuantity<=value2[2]:
                                                    historyFile.write(borrowerName+',')
                                                    historyFile.write(str(date)+',')
                                                    historyFile.write(str(key1)+',')
                                                    count = 0
                                                    for j in range(len(value2)):
                                                        if j == count:
                                                            bookName = value2[j]
                                                            billFile.write('Book Name :'+str(bookName)+'\n')
                                                            #historyFile.write(str(bookName)+',')
                                                            print('Book Name :',bookName)
                                                            count1 = count + 1
                                                        elif j == count1:
                                                            authorName = value2[j]
                                                            billFile.write('Author Name :'+str(authorName)+'\n')
                                                            print('Author Name :',authorName)
                                                            count2 = count1 + 1
                                                        elif j==count2:
                                                            quantity = value2[j]
                                                            historyFile.write(str(quantity)+',')
                                                            print('Quantity :',quantity)
                                                            if quantity == 0:
                                                                print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                                print('Available stock in our libary is :',quantity)
                                                                print()
                                                                break
                                                            else:
                                                                if clientQuantity<=quantity:
                                                                    remainingQuantity = quantity-clientQuantity
                                                                    billFile.write('Client Quantity :'+str(clientQuantity) +'\n')
                                                                    historyFile.write(str(clientQuantity)+',')
                                                                    historyFile.write(str(remainingQuantity)+',')
                                                                    print('Remaining Quantity',remainingQuantity)
                                                                    value2[j]=remainingQuantity
                                                                    count3 = count2 + 1
                                                                else:
                                                                    print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                                    print('Available stock in our libary is :',quantity)
                                                                    print()
                                                        elif j==count3:
                                                            price = value2[j]
                                                            print('Price($) :',price)
                                                            totalPrice = clientQuantity*price
                                                            billFile.write('Total Price($) :'+str(totalPrice)+'\n')
                                                            historyFile.write(str(totalPrice)+'\n')
                                                            billList.append(totalPrice)
                                                            print('Total Price',totalPrice)
                                                            billFile.write('===================='+'\n')
                                                            clientValue = True
                                                        else:
                                                            print('Index out of bound')  
                                                elif clientQuantity == 0:
                                                    print("Please enter the valid amount of quantity which is above 0")
                                                    clientValue = False
                                                else:
                                                    print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                    print('Available stock in our libary is :',value2[2])
                                                    print()
                                                    clientValue = True
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
                a = 0
                while a <= num:
                    a = a + 1
                    #historyFile.write(borrowerName  + ',')
                    #historyFile.write(str(date)+',')
                    keysValue = False
                    while keysValue == False:
                        try:
                            print('Choose a Book-ID from 1 to 10')
                            key1 = int(input('Enter the Book-ID that you want to borrow :'))
                            file5 = open('stock.txt','r')
                            if key1 > 0 and key1 < 11:
                                #historyFile.write(str(key1) + ',')
                                clientValue = False
                                while clientValue == False:
                                    try:
                                        clientQuantity = int(input('What quantity of book do you want to borrow from our libary ?\n'))
                                        for key, value2 in dicFile.items():
                                            if key1 == key:
                                                if clientQuantity > 0 and clientQuantity<=value2[2]:
                                                    historyFile.write(borrowerName  + ',')
                                                    historyFile.write(str(date)+',')
                                                    historyFile.write(str(key1) + ',')
                                                    count = 0
                                                    for j in range(len(value2)):
                                                        if j == count:
                                                            bookName = value2[j]
                                                            billFile.write('Book Name :'+str(bookName)+'\n')
                                                            #historyFile.write(str(bookName)+',')
                                                            print('Book Name :',bookName)
                                                            count1 = count + 1
                                                        elif j == count1:
                                                            authorName = value2[j]
                                                            billFile.write('Author Name :'+str(authorName)+'\n')
                                                            print('Author Name :',authorName)
                                                            count2 = count1 + 1
                                                        elif j==count2:
                                                            quantity = value2[j]
                                                            historyFile.write(str(quantity)+',')
                                                            print('Quantity :',quantity)
                                                            if quantity == 0:
                                                                print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                                print('Available stock in our libary is :',quantity)
                                                                print()
                                                                break
                                                            else:
                                                                if clientQuantity<=quantity:
                                                                    remainingQuantity = quantity-clientQuantity
                                                                    billFile.write('Client Quantity :'+str(clientQuantity) +'\n')
                                                                    historyFile.write(str(clientQuantity)+',')
                                                                    historyFile.write(str(remainingQuantity)+',')
                                                                    print('Remaining Quantity',remainingQuantity)
                                                                    value2[j]=remainingQuantity
                                                                    count3 = count2 + 1
                                                                else:
                                                                    print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                                    print('Available stock in our libary is :',quantity)
                                                                    print()
                                                        elif j==count3:
                                                            price = value2[j]
                                                            print('Price($) :',price)
                                                            totalPrice = clientQuantity*price
                                                            billFile.write('Total Price($) :'+str(totalPrice)+'\n')
                                                            historyFile.write(str(totalPrice)+'\n')
                                                            billList.append(totalPrice)
                                                            print('Total Price',totalPrice)
                                                            billFile.write('===================='+'\n')
                                                            clientValue = True
                                                        else:
                                                            print('Index out of bound')  
                                                elif clientQuantity == 0:
                                                    print("Please enter the valid amount of quantity which is above 0")
                                                    clientValue = False
                                                else:
                                                    print('Sorry, the qunatity of book that you have demand in our libary is insufficient.')
                                                    print('Available stock in our libary is :',value2[2])
                                                    print()
                                                    clientValue = True
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
    #historyFile.close()
    totalSum = 0
    for i in range(len(billList)):
        totalSum = totalSum + billList[i]
    billFile.write('Total Price of book is ($) :'+str(totalSum)+'\n')
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
    historyFile.close()
    Module_1_Read_Display_File.readDisplayFile()
    Module_3_Main_Transaction_Part.transaction()
