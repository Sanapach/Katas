#https://www.codewars.com/kata/5262119038c0985a5b00029f/
import math 
def is_prime(num):
    if num<=1:
        return False
    if num!=5 and str(num)[-1] == 0 or str(num)[-1] == 5:
        print("false")
        return False   
    if num!=2 and num%2 == 0:
        print("false")
        return False     
    result = [element for element in range(2,round(math.sqrt(num))) if num % element == 0 ]
    if len(result)>0:
        return False
    else: return True

is_prime(149)


