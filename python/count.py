#https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(s):
    arr=s.split(" ")
    dir ={}
    i=0
    while i<=len(s)-1:
        if arr[0][i] not in dir:
            dir[arr[0][i]]=1
        else: dir[arr[0][i]]+=1
        i+=1
    print(dir)


count("")