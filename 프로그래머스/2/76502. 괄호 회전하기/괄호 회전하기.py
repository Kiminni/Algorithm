def solution(s):
    answer = 0
    n = len(s)
    new_s = s[:]
    # 문자열 길이만큼 반복
    for _ in range(n):
        # 유효한지 판별
        if isValid(new_s):
            answer += 1
        # 괄호 회전하기    
        new_s = new_s[1:] + new_s[0]
        
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
            