
class IntegerNum:
    'osztály szintű adattag'

    def __init__(self,p1):
        self.number = p1

    def doubleNum(self):
        return self.number*2

    def squareNum(self):
        return self.number**2

    def pow(self,k):
        return self.number**k

    def abs(self):
        if self.number > 0:
            return self.number
        elif self.number < 0:
            return -self.number
        else:
            return 0


class Circle:
    'osztályszintű adattag:'
    pi = 3.14
    valami = 0

    def __init__(self,r):
        self.radius = IntegerNum(r)
        self.name = 'Kör'
        self.diameter = IntegerNum(2*r)

    def __str__(self):
        return "This circle has radius: {} and its area: {}".format(self.radius.number,self.area())

    def area(self):
        return self.radius.squareNum()*self.pi

    def perimeter(self):
        return self.radius.doubleNum()*self.pi


class MyString:

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input('Give me a string:')

    def printString(self):
        print(self.str.upper())


class SpecialElementsOfList:

    def __init__(self,ls):
        self.list = ls
        self.__length = len(ls)

    def getSumZeroSubLists(self):
        resLs = []
        tmpLs = []
        for i in range(0,self.__length):
            for j in range(i+1,self.__length):
                for k in range(j+1,self.__length):
                    tmpLs.append(self.list[i])
                    tmpLs.append(self.list[j])
                    tmpLs.append(self.list[k])
                    if sum(tmpLs) == 0:
                        resLs.append(tmpLs)
                    tmpLs = []
        return resLs



#MAIN
c1 = Circle(5)
c2 = Circle(7)

print(c1.__str__())
print(c2.__str__())

c1.radius=IntNumber(27)

print(c1.getArea())
print(c2.getPerimeter())

print(dir(c2))

str = 'english'
print(str.upper())

specLS = SpecialElementsOfList([-25, -10, -7, -3, 2, 4, 8, 10])
print(specLS.list)
print(specLS.getSumZeroSubLists())
