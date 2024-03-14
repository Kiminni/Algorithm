def solution(n, m):
    answer = 0
    minimum = []
    maximum = []
    
    for i in range (1, min(n,m) + 1):
        if n % i == 0 and m % i == 0 :
            minimum.append(i)
            
    for i in range(min(n, m), n * m + 1):    
        if i % n == 0 and i % m == 0:
            maximum.append(i)
            break
    
    return [max(minimum), maximum[0]]