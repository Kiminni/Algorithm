def solution(s):
    stack = []
    for i in s:
        if stack == [] and i == ")":
            return False
        elif i == "(":
            stack.append(i)
        elif i == ")" and stack != []:
            stack.pop()
    
    if stack != []:
        return False

    return True