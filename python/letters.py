#https://www.codewars.com/kata/59706036f6e5d1e22d000016/
def words_to_marks(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    array = [elements for elements in range(1, len(alphabet)+1)]

    result = 0
    for char in s:
        result += array[alphabet.index(char)]

    return result
