#https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python
def valid_braces(string):
    stack = []
    dikt = {")":"(","]":"[","}":"{"}
    for elements in string:
        if elements in dikt.values():
            stack.append(elements)
        elif elements in dikt.keys():
            if not stack or stack[-1] != dikt[elements]:
                return False
            stack.pop()
    return not stack