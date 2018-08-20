import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        z1 = self.real + no.real
        z2 = self.imaginary + no.imaginary
        return Complex(z1,z2)

    def __sub__(self, no):
        z1 = self.real - no.real
        z2 = self.imaginary - no.imaginary
        return Complex(z1,z2)

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        z1 = a*c - b*d
        z2 = a*d + b*c
        return Complex(z1,z2)

    def __truediv__(self, no):
        a = pow(no.real,2)+ pow(no.imaginary,2)
        return self*(Complex(no.real/a,-no.imaginary/a))

    def mod(self):
        return Complex(abs(complex(self.real,self.imaginary)),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')