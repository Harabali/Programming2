class PhoneNumberFormatException (Exception):
    pass

class EmailFormatException (Exception):
    pass

class MissingDataException(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "The " + self.__value + " text box is empty. You should provide this mandatory data!"

class Worker:

    def __init__(self,name,id,address,phone,email):
        self.__name = name
        self.__id = id
        self.__address = address
        self.__phone = phone
        self.__email = email

    def getName(self):
        return self.__name

    def setName(self,p):
        self.__name = p

    def getID(self):
        return self.__id

    def getAddress(self):
        return self.__address

    def setAddress(self,p):
        self.__address = p

    def getPhone(self):
        return self.__phone

    def setPhone(self,p):
        self.__phone = p

    def getEmail(self):
        return self.__email

    def setEmail(self,p):
        self.__email = p

    def __str__(self):
        return self.__name + '(ID: ' + self.__id + ')'

    def __le__(self, other):
        if self.getName() == other.getName():
            return self.getID() < other.getID()
        else:
            return self.getName() < other.getName()

    def __gt__(self, other):
        return self.getName() > other.getName()

    def __eq__(self, other):
        return self.getID() == other.getID()
