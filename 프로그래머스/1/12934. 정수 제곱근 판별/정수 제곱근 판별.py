# import math

# def solution(n):
#     result = math.sqrt(n)
#     if result % 1 != 0 :
#         return -1 
#     return (result+1) ** 2

def solution(n) :
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    
    return -1

    