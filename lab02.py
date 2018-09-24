
class IntNumber:
    def __init__(self,n):
        self.number = n

    def getSquare(self):
        return self.number**2

    def getSquareRoot(self):
        return self.number**(1/2)

    def getAbs(self):
        if self.number>0:
            return self.number
        elif self.number<0:
            return -self.number
        else:
            return 0


class Circle:
    'to here we should define the class variables like:'
    pi = 3.14

    def __init__(self,r):
        self.radius = IntNumber(r)
        self.diameter = 2*self.radius.number

    def __str__(self):
        return 'This circle has radius = {} and its area is: {}'.format(self.radius.number,self.getArea())

    def getArea(self):
        return self.radius.getSquare()*Circle.pi

    def getPerimeter(self):
        return 2*self.radius.number*Circle.pi

class MyString:
    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Give me a string: ')

    def printString(self):
        print(self.string.upper())


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
