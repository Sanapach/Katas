#https://www.codewars.com/kata/636f26f52aae8fcf3fa35819/
import sys
def total_bytes(obj):
    size = sys.getsizeof(obj)
    return (size)

total_bytes("hello")