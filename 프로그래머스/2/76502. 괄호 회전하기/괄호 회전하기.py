def solution(s):
    answer = 0
    n = len(s)
    new_s = s + s
    
    # 문자열 길이만큼 반복
    for i in range(n):
        # 유효한지 판별
        if isValid(new_s[i:i+n]):
            answer += 1
        # 괄호 회전하기    
        
    return answer


def isValid(s):
    stack = []
    dic = {
        "(":")",
        "{":"}", 
        "[":"]"    
    }
    for p in s:
        # 열린 괄호 => push
        # 닫힌 괄호 => pop
        if p in dic:
            stack.append(p)
        else:
            if not stack or dic[stack[-1]] != p:
                return False

            elif stack and dic[stack[-1]] == p:
                stack.pop()
            
            
    return not stack
            