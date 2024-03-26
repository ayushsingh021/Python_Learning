# try ... except
# Exception as e ads the error msg
def division (a,b):
    return a/b

try:
    val = division(40,0)
    print(val)
except Exception as e:
    print("Something went wrong" , e)
