#To write multiple lines of content you use the writelines() function. You use the write() function to add one line of content and the open() function to create, write or read a file.  

# with open('newText.txt' , mode = 'w') as file:
#      file.write('Hii i am Ayush')

try:
     with open('sample/new.txt' , mode = 'a') as file:
            file.writelines("\n i am new ")
except FileNotFoundError as e:
      print("Error : ", e)