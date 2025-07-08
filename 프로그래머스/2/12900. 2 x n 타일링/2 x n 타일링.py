def solution(n):
    ans = [1, 2]
    for i in range(2, n + 1):
        ans.append((ans[i - 1] + ans[i - 2]) % 1000000007)
    return ans[n - 1] 