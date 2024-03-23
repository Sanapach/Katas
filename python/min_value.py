#https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
def min_value(digits):
    string=list(set(digits))
    string.sort()
    s=[str(i) for i in string]
    return int("".join(s))

min_value([4, 7, 5, 7])