"""
실패율 = 클리어 X 유저 수 / 스테이지 도달한 플레이어 수
전체 스테이지 개수 N, 멈춘 번호 stages
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담긴 배열 return

스테이지의 개수 1 ~ 500
길이 1 ~ 200000 => 반복문 한 번
스테이지 => 1 ~ N + 1
실패율 같다 = 작은 번호 스테이지
도달한 유저가 없다 => 실패율 0
"""

def solution(N, stages):
    ratio = {}
    player = len(stages)
    
    for i in range(1, N + 1):
        if player == 0:
            ratio[i] = 0
    
        else:
            ratio[i] = stages.count(i) / player
            player = player - stages.count(i)
            
    sorted_ratio = sorted(ratio, key=lambda x: ratio[x], reverse=True)
    
    return sorted_ratio

    
    