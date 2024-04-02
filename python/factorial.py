#https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
import math
def factorial(n):
    result = [numbers for numbers in range(n+1)]
    result.pop(0)
    return math.prod(result)
factorial(5)