#https://www.codewars.com/kata/5839edaa6754d6fec10000a2/
def find_missing_letter(chars):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars1 = [x.lower() for x in chars]
    positions = zip(alphabet, range(26)) 
    start = dict(positions).get(chars1[0].lower())
    positions = zip(alphabet, range(26)) 
    finish=dict(positions).get(chars1[-1].lower())
    result=list(set((alphabet[start:finish])) - set(chars1))
    if chars[0].isupper():
        return [x.upper() for x in result][0]
    else: return result[0]
    

find_missing_letter(['O','Q','R','S'])