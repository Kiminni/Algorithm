def solution(num, total):
    answer = [0] * num
    mid = total // num
    i = 0
    for idx in range(mid-(num-1)//2, mid+(num+2)//2):
        answer[i] = idx
        i += 1
    return answer