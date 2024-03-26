# keyword arg -- kwargs

# def sum(a,b):
#     return a+b
# print(sum(4,5 , 6))  # will throw error cause we used excess arguments 

# args comes handy
#########   args ##############
def sumn(*args):
    sum = 0
    for val in args:
        sum += val
    return sum

print("Any num of elem add :" , sumn(5,4,6))

###########  kwargs ############

def sum_of (**kwargs):
    sum = 0
    for key,val in kwargs.items():
        sum +=val
    return sum

print(sum_of( coffee = 2 , rice = 5 , bread = 7.6))

