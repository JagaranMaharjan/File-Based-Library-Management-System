#readDisplayFile is a function which donot have any parameter and no return type
def readDisplayFile():
   print('==========================================Library Management System===================================================')
   print('\n\t\t\t\t\tAvailable Books In Library\t\t\t\t')
   print('======================================================================================================================')
   print('Book-ID\t\tBook Name\t\t\t\tAuthor Name\t\t\tQuantity\t\tPrice')
   print('======================================================================================================================')
   # open is a keyword that is used to open the file of a specific location.
   # r is a read mode that is used to read the text of the file
   file = open('stock.txt','r')
   key = 1
   #for line in file is used to read line by line
   for line in file:
      #replace is a keyword that is used to replace by horizontal tab(\t) instead of comma
      print(' ', key, '\t\t'+ line.replace(',','\t\t\t'))
      key = key + 1
      print('----------------------------------------------------------------------------------------------------------------------')
   print('======================================================================================================================')
