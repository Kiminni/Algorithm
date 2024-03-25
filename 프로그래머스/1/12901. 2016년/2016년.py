import datetime
def solution(a, b):
    
    month = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    date = b
    for i in range(a-1):
        date +=month[i]

    return day[date%7]