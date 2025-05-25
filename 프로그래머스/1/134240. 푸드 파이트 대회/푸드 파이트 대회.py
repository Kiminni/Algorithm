"""
1. 왼쪽->오른쪽으로 음식을 먹는다.
2. 중앙에 물을 배치.
3. 그거의 역순으로 배치
"""
def solution(food):
    """
    1. 각 값을 2로 나누었을 때, 몫이 0인지 아닌지 확인
    2. 나머지가 0인지, 아닌지를 확인해서 1을 뺄지 그대로 할지 확인 => 관련 값을 리스트에 저장
    3. 위 리스트를 토대로 지정 + 0 + 반대로 지정 
    """
    
    answer = ""
    tmp = []
    for i in range(len(food)):
        for j in range(food[i] // 2):
            tmp.append(str(i))
    
    return ''.join(tmp) + '0' + ''.join(reversed(tmp))