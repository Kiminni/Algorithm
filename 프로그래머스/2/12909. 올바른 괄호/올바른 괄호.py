def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and stack == []:
            return False
        elif i == ")" and stack != []:
            stack.pop()
    
    if stack != []:
        return False
    
    return True
    