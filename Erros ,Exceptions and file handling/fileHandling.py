# two file handling functions in python  ---- open() and close()

##############  OPEN #########################
# open --- readinf writing and creating file
# open(<FILE NAME> <FILE LOCATION> , <MODE>)  --->takes two argus
# Mode - 'r' (open and read in text format) and Mode - 'rb' (open and read in binary format)
#  Mode - 'r+' (open for reading and writing) and Mode - 'w' (open for writing)
# open(<FILE NAME , a) -->(open for editing and appending data)

############    CLOSE #########################
# close() --- takes no arguments

# gen in python we handle file in two ways either in 'txt' or 'binary' -- txt is by default

# if the prog and txt file is in same folder no need to give the directory

with open('sample.txt', mode ='r') as file:  ## no close function req for this syntax
    # Indented block where you perform operations on the file
    data = file.read()
    # Process the data or perform other operations

print(type(data))
print(data)
  

userData = open('test.txt' , mode = 'r')
data = userData.readline()
print(data)
userData.close()