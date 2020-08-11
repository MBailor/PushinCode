


#Parent Class is Banker
class Banker:
    name = "Billy"
    department = "Manager"
    empNum = "3809"

#           This is the method of the parent class
    def loginInfo(self):
        entry_name = input("Employee Name: \n")
        entry_department = input("Job Title: \n")
        entry_empNum = input("Employee Number: \n")
        if (entry_department == self.department and entry_empNum == self.empNum):
            print("Welcome back, {} Now GET BACK TO WORK!\n".format(entry_name))
        else:
            print("Incorrect Employee Number. Security has been notified!!\n")

class Underling(Banker):
    name = "Jimmy"
    department = "Teller"
    email = "JWe@mail.com"
    empPin = "2445"

    def loginInfo(self):
        entry_name = input("Employee Name: \n")
        entry_department = input("Job Title: \n")
        entry_empPin = input("Employee Number: \n")
        if (entry_department == self.department and entry_empPin == self.empPin):
            print("Welcome back, {} Now GET BACK TO WORK!\n".format(entry_name))
        else:
            print("Incorrect Employee Number. Security has been notified!!\n")
    

class Member(Banker):
    userName = "Marcy"
    department = ""
    email = "JWe@mail.com"
    pinNum = "2890"

    def loginInfo(self):
        entry_userName = input("Member Name: \n")
        entry_department = input("Who would you like to see, Manager or Teller? \n")
        entry_pinNum = input("Enter Pin Number: \n")
        if (entry_department == "Teller"): 
            print("Welcome back, {}! Jimmy will be with you shortly \n".format(entry_userName))
        elif (entry_department == "Manager"):
            print("Welcome back, {}! Billy will be with you shortly \n".format(entry_userName))
        else:
            print ("User Name, Pin Number, or desired employee incorrect. Goodbye")



parents = Banker()
parents.loginInfo()

kiddo = Underling()
kiddo.loginInfo()

kiddo1 = Member()
kiddo1.loginInfo()
