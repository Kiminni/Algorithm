def solution(s):
    stack = []
    for i in s:
        if not stack and i == ")":
            return False
        if i == "(":
            stack.append(i)  
        if stack and i == ")":
            stack.pop()
    
    return stack == []