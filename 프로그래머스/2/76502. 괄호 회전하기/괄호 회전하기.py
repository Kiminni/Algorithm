from collections import deque
def solution(s):
    answer = 0
    dic = {
        "(":")",
        "{":"}", 
        "[":"]"    
    }
    d = deque(s)
    for i in range(len(s)):
        stack = []
        tmp = d.popleft()
        d.append(tmp)
        for j in range(len(d)):
            if d[j] in dic:
                stack.append(d[j])
            elif stack == [] and d[j] in dic.values():
                stack.append(d[j])
                break
            if stack != [] and d[j] in dic.values():
                if dic[stack[-1]] == d[j]:
                    stack.pop()
        if stack == [] and j == len(d) - 1:
            answer += 1
    return answer