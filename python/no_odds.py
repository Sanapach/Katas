#https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
def no_odds(values):
    #result = [element for element in values if element % 2 == 0] alt way

    result = []
    for element in values:
        if element%2 ==0:
            result.append(element)
    return result


no_odds([])  