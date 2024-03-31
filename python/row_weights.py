#https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python
def row_weights(array):
    # array[1::2] even numbers
    arr =(sum(array[::2]),sum(array[1::2]))

    print(arr)

row_weights([13,27,49])