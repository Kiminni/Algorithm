def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    real_lost = []
    real_reserve = []
    
    for l in lost:
        if l not in reserve:
            real_lost.append(l)
        else:
            reserve.remove(l)  
    
    for r in real_reserve + reserve:
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)
    
    return n - len(real_lost)