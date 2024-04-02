#https://www.codewars.com/kata/58552bdb68b034a1a80001fb/
import math
def cook_pancakes(n, m):
    if n<m:
        result=math.ceil((n*2)/(m-(m-n)))
        return result
    else:
        result=math.ceil((n*2)/(m))
        return result


cook_pancakes(1,4)



