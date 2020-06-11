# dictionaryFileList is a type of function which has no parameter but return type value
def dictionaryFileList():
   #open is a keyword that is use to open the file of a specific location
   # r is a read mode that is used to read a line
   bookInfo = open('stock.txt','r')
   #declare a dictionary 
   dictionaryBookData = {}
   counter = 1
   #for line in bookInfo is used to read a line of text line by line
   for line in bookInfo:
      #replace is used to replace by '' instead of \n
      line1 = line.replace('\n','')
      #replace is used to replace the $ sign by ''
      line2 = line1.replace('$','')
      #dictionaryBookData[counter] it is used to set the key of dictionary
      dictionaryBookData[counter] = line2.split(',')
      counter = counter + 1
   #accessing the values of dictionary
   for value in dictionaryBookData.values():
      #2 is the starting pont, len(value)-1 is ending point
      for j in range(2, len(value)):
           if j==2:
              #if j==2 then assign the new value[j] as int(value[j])
                value[j] = int(value[j])
                #print(value[j])
           elif j==3:
              # if j==3 then assign the new value[j] as float(value[j])
                value[j] = float(value[j])
                #print(value[j])
      # return is a keyword that is used to return the value of dictionary
   return dictionaryBookData


