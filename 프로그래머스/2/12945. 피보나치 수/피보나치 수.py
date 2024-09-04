def solution(n):
    dp = [0] * (n+1)
    def fibo(n):
        dp[2] = 1
        dp[3] = 2
        
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    return fibo(n) % 1234567