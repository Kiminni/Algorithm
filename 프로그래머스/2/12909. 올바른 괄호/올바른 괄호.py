"""
1. 문자열을 하나씩 stack에 집어 넣고
2. 어차피 ( 아니면 ) 이니까 왼쪽이면 left + 1, 오른쪽이면 right + 1
"""
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and stack == []:
            return False
        elif i == ")" and "(" in stack:
            stack.pop()
                 
    if stack == []:
        return True
    
    return False
        
    
    