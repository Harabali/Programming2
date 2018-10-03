import numpy as np

class ParentClass (object):
    pass

class ChildClass(ParentClass):
    pass

ch = ChildClass()
c = ParentClass()

print(ChildClass.__bases__)
print(ParentClass.__bases__)
print(object.__bases__)

print(ch.__class__)
print(isinstance(c,ChildClass))


class Polygon:

    def __init__(self,p1=0):
        self.n = p1
        self.sides = [0.0 for x in range(p1)]

    def inputSides(self):
        for i in range(0,len(self.sides)):
            self.sides[i] = int(input('Give the length of {}. side:'.format(i+1)))

    def printSides(self):
        for i in range(0,len(self.sides)):
            print('The {}. side is {} length.'.format(i+1,self.sides[i]))

class Triangle (Polygon):

    def __init__(self):
        Polygon.__init__(self,3)


    def getPerimeter(self):
        P = 0
        for i in self.sides:
            P += i
        return float(P)

    def getArea(self):
        s = self.getPerimeter()/2
        A = s
        for i in self.sides:
            A*=float(s-i)
        return A**0.5



tmp = Triangle()
tmp.inputSides()
tmp.printSides()
print(tmp.getArea())


class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def __str__(self):
        return "The balance of this bank account is: {}".format(self.balance)


class PreDeterminedMinAccount(BankAccount):

    def __init__(self,p1):
        BankAccount.__init__(self)
        self.minLimit = -p1

    def withdraw(self,amount):
        if self.balance - amount >= self.minLimit:
            super().deposit(amount)
        else:
            print("Unfortunately, you reached the pre-defined limit.")


c = PreDeterminedMinAccount(100)
for i in range(1,15):
    if int(np.random.randint(0,2))==0:
        c.withdraw(int(np.random.randint(1,100)))
    else:
        c.deposit(int(np.random.randint(1,100)))
    print(c)

class MyList(list):

    def __init__(self,p1):
        list.__init__(self,p1)

    def clear(self):
        tmp = self.copy()
        for i in tmp:
            if i<0:
                self.remove(i)

l = MyList(np.random.randint(-20,20,20))
l.clear()
print(l)