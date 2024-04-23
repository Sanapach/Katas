#https://www.codewars.com/kata/5aff237c578a14752d0035ae/

import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    print(int((math.sqrt((age_1*age_1)+(age_2*age_2)+(age_3*age_3)+(age_4*age_4)+(age_5*age_5)+(age_6*age_6)+(age_7*age_7)+(age_8*age_8)))/2))

predict_age(65,60,75,55,60,63,64,45)

# def predict_age(*ages):
#     return sum(a*a for a in ages)**.5//2