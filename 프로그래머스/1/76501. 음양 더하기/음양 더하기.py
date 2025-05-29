"""
정수 배열 / 절댓값 배열
이걸 실제로 접근해서 해결하는 문제
[4, 7, 12]
[t, f, t]
-> +4 -7 +12

len(signs) == len(absolutes)

반복문을 실행을 해야합니다. 둘의 길이 중 하나를 갖고 반복문을 돌릴겁니다.
이 때, 이 과정에서 중요한 것은 true인지, false인지를 확인 후 값을 더한다.
"""
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    
    return answer