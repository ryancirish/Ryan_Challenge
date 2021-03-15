import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        img = self.imaginary + no.imaginary
        return Complex(real, img)        
        
    def __sub__(self, no):
        real = self.real - no.real
        img = self.imaginary - no.imaginary
        return Complex(real, img)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        img = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, img)

    def __truediv__(self, no):
        conjugate_real = no.real  
        conjugate_imaginary = -no.imaginary

        one = self.real * conjugate_real - self.imaginary * conjugate_imaginary
        two = self.real * conjugate_imaginary + self.imaginary * conjugate_real        
        denominator = no.real ** 2 + no.imaginary ** 2
        
        real = one / denominator
        img = two / denominator
        return Complex(real, img)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

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