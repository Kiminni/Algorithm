from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    # while q:
    #     m = max(q) # 가장 높은 우선순위 값 저장
    #     l = q.popleft()
    #     location -= 1 # 하나가 빠졌으니까 location도 빠짐
    #     if l != m : # 가장 높은 우선순위 값과 현재 맨 왼쪽의 값과 다르다
    #         q.append(l) # 다시 넣는다.
    #         if location < 0 : # location이 0보다 작아진다면
    #             location = len(q) - 1 #얘도 초기화
    #     else: # 가장 앞 프로세스가 가장 높은 우선순위
    #         answer += 1 
    #         if location < 0 :
    #             break
    
    while q:
        m = max(q)
        l = q.popleft()
        location -= 1
        if l != m :
            q.append(l)
            if location < 0 :
                location = len(q) - 1
        else:
            answer += 1
            if location < 0:
                break
                
    
    return answer
    