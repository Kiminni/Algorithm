def solution(n):
    answer = 0
    prime = [True] * (n+1)
    for i in range(2, n+1):
        if prime[i] == True:
            for j in range(i+i, n+1, i): #배수 생략
                prime[j] = False
    
    for i in range(2, n+1):
        if(prime[i] == True):
            answer += 1
    return answer