def solution(s):
    stack = []
    for i in s:
        if i == ")" and stack == []:
            return False
        elif i == "(":
            stack.append(i)
        elif i == ")" and "(" in stack:
            stack.pop()
    
    if stack != []:
        return False
    
    return True