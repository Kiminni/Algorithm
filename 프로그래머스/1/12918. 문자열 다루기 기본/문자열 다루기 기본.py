# 문자열의 길이가 4이거나, 6인지 확인한다.
# 문자열이 숫자로만 구성되어있는지를 확인한다.
# 이 때, 알파벳 같은 경우는 a, A 총 2가지의 경우가 있을 수 있으니 소문자로 바꾼다.
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for string in s:
        if string.lower() in "abcdefghijklmnopqrstuvwxyz":
            return False
        
    return True
    