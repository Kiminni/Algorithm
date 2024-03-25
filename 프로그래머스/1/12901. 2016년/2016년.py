import datetime
def solution(a, b):
    
    cal_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return cal_list[datetime.datetime(2016, a, b).weekday()]