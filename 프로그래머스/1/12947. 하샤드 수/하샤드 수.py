def solution(x):
    N = [int(i) for i in str(x)]
    if x % sum(N) == 0:
        return True
    
    return False