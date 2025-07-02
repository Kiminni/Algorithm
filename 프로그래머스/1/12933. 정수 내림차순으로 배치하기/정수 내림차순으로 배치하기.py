def solution(n):
    list_n = list(str(n))
    tmp = []
    for l in list_n:    
        tmp.append(int(l))
    
    tmp.sort(reverse=True)
    ans = ""
    for m in tmp:
        ans += str(m)
    return int(ans)
    