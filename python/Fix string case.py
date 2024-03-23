#https://www.codewars.com/kata/5b180e9fedaa564a7000009a
def solve(s):
    i=0
    counter=0
    while i<=len(s)-1:
        if s[i].isupper() == True:
            counter+=1
        else:
            counter-=1
        i+=1
    if counter>0:
        return (s.upper())
    else: return (s.lower())
solve("coDE")