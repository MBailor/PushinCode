


#Parent Class is Banker
class Banker:
    name = "Jimmy"
    department = "Teller"
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

#Child Class is Member
class Member:
    name = "Dirk"
    birthPlace = "Seattle"
    pinNum = "2445"

#           Same method that the parent uses except parent asked for employee number and child askes for a pin number
    def loginInfo(self):
        entry_name = input("Enter Member Name: \n")
        entry_birthPlace = input("City of Birth: \n")
        entry_pinNum = input("Enter Pin Number: \n")
        if (entry_birthPlace == self.birthPlace and entry_pinNum == self.pinNum):
            print("Welcome back, {} Let's do some Banking!, for a nominal fee\n".format(entry_name))
        else:
            print("Incorrect Pin Number. Card will be retained and security and local law enforcement are enroute!!\n")

class ArmorCar:
    driver = "Ted"
    mover = "James"
    truckNum = "0459"


    def loginInfo(self):
        entry_driver = input("Enter Drivers Name: \n")
        entry_mover = input("Enter Name of Money Mover: \n")
        entry_truckNum = input("Enter Truck Number: \n")
        if (entry_truckNum == self.truckNum and entry_mover == self.mover):
            print("Welcome back, {}! Thanks for keeping our Money safe\n".format(entry_mover))
        else:
            print("You are not, {}. Access to vault denied. Security and local law enforcement are enroute and YOU WILL BE SHOT!!\n".format(entry_mover))

#  This code called the methods written above
worker = Banker()
worker.loginInfo()

bmember = Member()
bmember.loginInfo()

armorm = ArmorCar()
armorm.loginInfo()
