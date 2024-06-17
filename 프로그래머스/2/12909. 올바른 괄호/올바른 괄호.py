def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and stack == []:
            return False
        elif "(" in stack and i == ")":
            stack.pop()
    
    if stack != []:
        return False
    return True
        