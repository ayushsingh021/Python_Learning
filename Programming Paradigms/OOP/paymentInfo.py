class Payment :
    #constructor
    def __init__(self , name , payment , amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    
    # self is equivalent to this
    def pay(self) :
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            print(self.name , " is paid " , self.amount )
        else :
            print(self.name + " not paid yet ")


#instances
ayush = Payment("Ayush" , "no" , 10000000)
raj = Payment("Raj" , "yes" , 40000)

print(ayush.status() ," \n" , raj.status())
ayush.pay() #the dunction changes the payment from no to yes
print(ayush.status())
