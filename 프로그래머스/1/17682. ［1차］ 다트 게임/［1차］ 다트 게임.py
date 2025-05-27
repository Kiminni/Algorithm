# 다트는 총 3번
# 0 ~ 10점
# S, D, T 영역 존재 -> 1제곱, 2제곱, 3제곱으로 계산
# * = 점수의 2배 / # = 점수의 -
# *은 첫번째에도 나오고, 다른 *과 중첩 -> 4배 이건 
# *과 #이 같이 붙으면, -2배가 된다.
# s, d, t는 점수마다 하나씩 존재
# *과 #은 둘 중 하나만 존재 가능

# 반복문을 통해서 s, d, t가 앞에 있는지를 확인하고, 리스트를 만들어서 거기에 넣는다.
def solution(dartResult):
    tmp = ""
    score = []
    for i in dartResult:
        if i.isnumeric():
            tmp += i
            
        elif i == "S":
            score.append(int(tmp) ** 1)
            tmp = ''
            
        elif i == "D":
            score.append(int(tmp) ** 2)
            tmp = ""
            
        elif i == "T":
            score.append(int(tmp) ** 3)
            tmp = ""
            
        elif i == "*":
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        
        elif i == "#":
            score[-1] *= (-1)
        
    return sum(score)
        