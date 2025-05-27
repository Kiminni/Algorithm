# s는 한 개 이상의 단어로 구성 각 단어에는 공백 문자
# 짝수번째는 대문자, 홀수번째는 소문자

# 짝 홀수 인덱스가 아니라, 공백 기준으로 짝 홀수를 처리
# 0번째 인덱스는 짝수 알파벳

# "try hello world" -> "TrY HeLlO WoRld" 
# T r Y // H e L l o
# 문자열을 쪼개서 리스트에 넣고
# 반복문을 진행할 때 새로이 문자열을 넣고
# 공백이 있다면 문자 마지막에 넣는 식으로 처리
def solution(s):
    string_list = s.split(" ") # ["try", "hello", "world"]
    temp = []
    for string in string_list: # ["try"]
        for i in range(len(string)):
            if i % 2 == 0:
                temp.append(string[i].upper())
            else:
                temp.append(string[i].lower())
        temp.append(" ")
    temp.pop()
    return ''.join(temp)
    
    
    