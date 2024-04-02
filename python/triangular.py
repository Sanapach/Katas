#https://www.codewars.com/kata/525e5a1cb735154b320002c8/solutions/python
from decimal import *
getcontext().prec = 1000
def triangular(n):
    if n<=0:
        return 0
    else:
        x = ((Decimal(n))-(Decimal(1)))*((Decimal(n))*(Decimal(0.5)))+Decimal(n)
    return Decimal(x)

