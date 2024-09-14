from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    answer = 0
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    for i in range(4 * (len(q1))):
        if q1_sum > q2_sum:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp
            answer += 1
            
        elif q2_sum > q1_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q2_sum -= tmp
            q1_sum += tmp
            answer += 1
        else:
            return answer
    
    if sum(q1) != sum(q2):
        return -1
    