#str[start : stop : step]

# Method : 1
# trial = "reversal"
# new_trial = trial[ : : -1]
# print(new_trial)

#Method : 2
def str_reversal(str):
    if(len(str) == 0):
        return str
    else:
        return str_reversal(str[1:]) + str[0]

str = "Ayush" 
newstr = str_reversal(str)
print(newstr)