import math

def solution(n):
    result = math.sqrt(n)
    if result % 1 != 0 :
        return -1 
    return (result+1) ** 2

    