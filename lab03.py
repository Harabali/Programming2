import math

class Triangle:

    def __init__(self,p1,p2,p3=0):
        if p3 == 0:
            self.a = p1
            self.h = p2
        else:
            self.a=p1
            self.b=p2
            self.c=p3

    def area(self):
        if hasattr(self,'c'):
            s = (self.a+self.b+self.c)/2
            area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
            return area
        else:
            return self.a*self.h/2

    def perimeter(self):
        if hasattr(self,'c'):
            return self.a+self.b+self.c
        else:
            return 'I cannot calculate the perimeter from two independent data.'

    def __str__(self):
        if hasattr(self,'c'):
            return 'This triangle has sides with length: ({},{},{})'.format(self.a,self.b,self.c)
        else:
            return 'This triangle has one side with {} length and high with {} length'.format(self.a,self.h)

    def __add__(self, other):
        if isinstance(other,Triangle):
            return self.area()+other.area()

        if isinstance(other,int) or isinstance(other,float):
            return self.area() + other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other,Triangle):
            return self.area()-other.area()

        if isinstance(other,int) or isinstance(other,float):
            return self.area() - other

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()


class Vector:
    origoX = 0
    origoy = 0

    def __init__(self,p1,p2):
        self.X = p1
        self.Y = p2

    def __str__(self):
        return '<{},{}>'.format(self.X,self.Y)

    def __abs__(self):
        return (self.X**2+self.Y**2)**0.5

    def __add__(self, other):
        if isinstance(other,Vector):
            x = self.X + other.X
            y = self.Y + other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X + other
            y = self.Y + other

        return self.__class__(x,y)

    # def __radd__(self, other):
    #     return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other,Vector):
            x = self.X + other.X
            y = self.Y + other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X + other
            y = self.Y + other

        self.X = x
        self.Y = y
        return self

    def __sub__(self, other):
        if isinstance(other,Vector):
            x = self.X - other.X
            y = self.Y - other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X - other
            y = self.Y - other

        return self.__class__(x,y)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other,Vector):
            return self.X*other.X+self.Y*other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X * other
            y = self.Y * other
            return self.__class__(x,y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.__abs__() == other.__abs__()

    def __ne__(self, other):
        return self.__abs__() != other.__abs__()

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __le__(self, other):
        return self.__abs__() <= other.__abs__()


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return "({}+{}j)".format(self.real,self.imag)

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def argz(self):
        return math.atan(self.imag / self.real)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag

        if isinstance(other, ComplexNumber):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag

        return self.__class__(real_part, imag_part)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other
            imag_part = self.imag

        if isinstance(other, ComplexNumber):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            real_part = self.real * other
            imag_part = self.imag * other

        if isinstance(other, ComplexNumber):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)

        return self.__class__(real_part, imag_part)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        # c1 - n != n - c1
        if isinstance(other, float) or isinstance(other, int):
            real_part = other - self.real
            imag_part = -self.imag

        return self.__class__(real_part, imag_part)

    def __eq__(self, other):
        # Note: generally, floats should not be compared directly
        # due to floating-point precision
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) or (self.imag != other.imag)


#MAIN>
t1 = Triangle(3,4,5)
print(t1)
print(t1.area())
t2 = Triangle(4,6)
print(t2)
print(t2.area())
print('The sum of the triangle is: ',t1+t2)
print(t1+10)
print(10+t1)
print('The diff of the triangle is: ',t1-t2)
print(t1!=t2)

v1 = Vector(3,4)
v2 = Vector(7,8)
print(v1)
print(abs(v1))
print(isinstance(5+v1,Vector))

v1+=7
print(v2,'-',v1,'=',v2-v1)
print(v2,'*',v1,'=',v2*v1)
print(v2,'*','14','=',v2*14)



print(v1>v2)

C1 = complex(5.3,3.2)
print(C1)