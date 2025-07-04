def solution(n):
    fib = [0, 1, 1, 2]
    for i in range(4, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
        
    return fib[n] % 1234567