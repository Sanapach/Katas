#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
def sum_of_minimums(numbers):
    result=[sorted(array)[0] for array in numbers ]
    print(sum(result))

sum_of_minimums([[11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]])