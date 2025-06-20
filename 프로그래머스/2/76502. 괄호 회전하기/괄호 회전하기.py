from collections import deque

def isValid(parent):
    stack = []
    dic = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    for p in parent:
        if p in dic.keys():
            stack.append(p)

        elif not stack and p not in dic.keys():
            return False

        elif dic[stack[-1]] == p and stack:
            stack.pop()

    return not stack

def solution(s):    
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        tmp = s.popleft()
        s.append(tmp)
        if isValid(s):
            answer += 1
    
    return answer