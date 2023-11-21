

def solution(dots):
    if inclination(dots[0],dots[1]) == inclination(dots[2],dots[3]):
        return 1
    
    if inclination(dots[2],dots[1]) == inclination(dots[0],dots[3]):
        return 1
    
    if inclination(dots[3],dots[1]) == inclination(dots[2],dots[0]):
        return 1
    
    return 0

def inclination(dot1, dot2):
    return (dot2[1] - dot1[1] ) / (dot2[0] - dot1[0])