#https://www.codewars.com/kata/52c31f8e6605bcc646000082
def two_sum(numbers, target):
    i=0
    empty_list=[]
    indices = [i for i in range(len(numbers)) if numbers[i]==target//2]
    while i<len(numbers):
        result = target - numbers[i]
        if result in numbers:
            if result == target//2:
                i+=1
                continue
            empty_list.append(numbers.index(numbers[i]))  
            empty_list.append(numbers.index(result))
        i+=1
    if len(indices)<2:
        return tuple(empty_list[:2])
    else:
        final=empty_list+indices
        return tuple(final[:2])

two_sum([26,21,14,4,2,10,9,12,24,5,10,5,22,25,29,11,12,16,7], 39)

# def two_sum(nums, t):
#     for i, x in enumerate(nums):
#         for j, y in enumerate(nums):
#             if i != j and x + y == t:
#                 return [i, j]
