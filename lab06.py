class Month:
    names = ['JAN','FEB','MARCH','APR','MAY','JUNE','JULY','AUGUST','SEPT','OCT','NOV','DEC']
    numOfdays = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self,number):
        self.__name = Month.names[number-1]
        self.__length = Month.numOfdays[number-1]

    def getName(self):
        return self.__name

    def getLength(self):
        return self.__length

    def __str__(self):
        return '{} is {} length'.format(self.__name,self.__length)

class NameDaysOfMonth(Month):

    def __init__(self,number):
        Month.__init__(self,number)
        self.__names = [0 for i in range(self.getLength())]

    def __str__(self):
        tmp = Month.__str__(self) +' and the day of names:\n'
        for i in range(len(self.__names)):
            tmp += '{}.: {}\n'.format(i+1, self.__names[i])
        return tmp

    def inputNames(self,inputFile="-1"):
        if inputFile == "-1":
            for i in range(len(self.__names)):
                tmp = input('Give me the names of {}. days:'.format(i+1))
                self.__names[i] = tmp.split(',')
        else:
            try:
                fin = open(inputFile,'r')
                ind = 0
                for line in fin:
                    start = line.find(':')
                    self.__names[ind] = line[start+1:-1].split(',')
                    ind += 1
            except FileNotFoundError:
                print('The given file is not found.')

    def getDayOfName(self,name):
        for i in range(len(self.__names)):
            if name in self.__names[i]:
                return i+1
        return -1

class Student:

    def __init__(self,firstName, familyName):
        self.__firstName = firstName
        self.__familyName = familyName

    def __str__(self):
        return self.__firstName + " " + self.__familyName

    def get_firstName(self):
        return self.__firstName

    def get_familyName(self):
        return self.__familyName

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_familyName(self, familyName):
        self.__familyName = familyName

    def __qe__(self, other):
        if self.__familyName == other.__familyName:
            return self.__firstName > other.__firstName
        else:
            return self.__familyName > other.__familyName

    def __lt__(self, other):
        return self.__familyName < other.__familyName

class SchoolClass:

    def __init__(self,id):
        self.__id = id
        self.__members = []

    def __str__(self):
        tmp = self.__id + ' class members:\n'
        for i in self.__members:
            tmp += i.__str__() + '\n'
        return tmp

    def inputMembers(self,fileIn = '-1'):
        if fileIn == -1:
            str = input("Give me the name of the new class mate:")
            tmp = str.split(" ")
            self.__members.append(Student(tmp[0],tmp[1]))
        else:
            try:
                fin = open(fileIn,'r')
                for line in fin:
                    tmp = line.split(" ")
                    self.__members.append(Student(tmp[1][:-1],tmp[0]))
            except FileNotFoundError:
                print('The given file is not found.')

    def getMember(self):
        return self.__members

    def __add__(self, other):
        for i in other.__members:
            self.__members.append(i)
        return self

#MAIN:
tmp = NameDaysOfMonth(4)
tmp.inputNames('AprilNames.txt')

sc = SchoolClass('12B')
sc.inputMembers('12B class.txt')

sc2 = SchoolClass('8A')
sc2.inputMembers('8A class.txt')

sc += sc2
print(sc)

#dictionary:
partys = {}
for i in sc.getMember():
    n = tmp.getDayOfName(i.get_firstName())
    if n != -1:
        if n in partys:
            partys[n].append(i)
            partys[n].sort()
        else:
            partys[n] = []
            partys[n].append(i)
            partys[n].sort()

for i in partys:
    if len(partys[i]) == 1:
        print(i,':',partys[i][0])
    else:
        print(i,':')
        for j in partys[i]:
            print("   :",j)