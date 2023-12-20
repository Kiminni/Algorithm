def solution(a, b):
    ans = 0
    if a > b: a,b = b,a
    for i in range(a, b + 1):
        ans += i
    return ans