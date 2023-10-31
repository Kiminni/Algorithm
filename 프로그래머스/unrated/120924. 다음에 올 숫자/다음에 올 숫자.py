def solution(common):
    answer = 0
    first = common[1] - common[0]
    second = common[2] - common[1]
    
    if first == second:
        return common[-1] + first
    
    elif (second / first) == (common[1] / common[0]):
        return common[-1] * (common[1]/common[0])