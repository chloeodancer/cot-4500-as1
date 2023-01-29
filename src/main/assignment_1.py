import math
import numpy as np

#1
def double_precision():
    s=0
    print(s)
    exponent = 10000000111
    c, i = 0,0
    while(exponent != 0):
        exp = exponent % 10
        c=c+exp*pow(2,i)
        exponent = exponent//10
        i+= 1
    print(c)
    fraction = str(11101011100100000000000000000000000000000000000000000)
    f=0
    i=1
    for item in fraction:
        f=f+int(item)*(0.5**i)
        i+=1
    print(f)
    n=((-1)**s)*(2**(c-1023))*((1+f))
    print(n)
    return
double_precision()

#2
n *= (10 ** -3)
print((math.floor(n*1000)) / 1000)
print()

#3
n += 0.0005
print(round(n, ndigits = 3))
print()

#4
def absolute_error(precise:float, approximate:float):
    sub_operation = precise - approximate
    return abs(sub_operation)
def relative_error(precise:float, approximate:float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation
print(absolute_error(491.5625, 492))
print(relative_error(491.5625, 492))
print("\n")

#5
def infiniteseries(x, k:int):
    return((-1)**k) * ((x**k)/(k**3))
minerror = 1e-4
currentit = 1
while(abs(infiniteseries(1, currentit))>minerror):
    currentit +=1
print(currentit - 1)
print("\n")

#6
def q_6():
    def function(x):
        return x*x*x - 4*x*x - 10
    def bisection(f, a, b, tol):
        if np.sign(f(a))==np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        m = (a+b)/2
        if np.abs(f(m))<tol:
            return m + 1
        elif np.sign(f(a))==np.sign(f(m)):
            return bisection(f, a, b, tol) + 1
        elif np.sign(f(b))==np.sign(f(m)):
            return bisection(f, a, b, tol) + 1
    def newton(f, df, x0, tol):
        result = f(x0) / df(x0)
        x = x0
        count = 1
        while(abs(result)>= tol):
            x-= result
            count += 1
            result = f(x) / df(x)
        return count
            
    f = lambda x: x*x*x - 4*x*x - 10
    f_prime = lambda x: 3*x*x + 8*x

    print(bisection(f, -4, 7, 0.0001 ))
    print(newton(f, f_prime, 7, 0.0001))
    print()

double_precision()
q_6()
