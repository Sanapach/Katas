#https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
def evaporator(content, evap_per_day, threshold):
    threshold = threshold/100
    evap_per_day= evap_per_day/100
    final_volume = content * threshold
    days=0
    while final_volume<content:
        content -= content * evap_per_day
        days+=1
    return days

evaporator(10,10,5)