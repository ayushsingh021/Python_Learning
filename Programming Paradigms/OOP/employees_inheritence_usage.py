#  Changes made to a child class do not extend to the parent class. but opposite is not true   
class Employees:
    def __init__(self,name ,surname) -> None:
        self.name = name
        self.surname = surname

class Supervisors(Employees):
    def __init__(self, name, surname, password) -> None:
        super().__init__(name, surname)
        self.password = password

class Chefs(Employees):
    def leave_req(self,days):
        return "May I take a leave for " + str(days) + " days"
    
adrian = Supervisors("Adrian" , "A" , "apple")

emily = Chefs("Emily" , "E")
juno = Chefs("Juno" , "J")



print(emily.leave_req(4))
print(emily.name)
print(adrian.password)

        