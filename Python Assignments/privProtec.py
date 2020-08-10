

# Protected
class Protec:
    def __init__(self):
        self._protecVar = 0

obj = Protec()
obj._protecVar = 17
print(obj._protecVar)


# Private
class Protect:
    def __init__(self):
        self.__privateVar = 245

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

# printing the private and protected variables

obj = Protect()
obj.getPrivate()
obj.setPrivate(985)
obj.getPrivate()

