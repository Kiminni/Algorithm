# arr 0 ~ 9
# 연속으로 주어진 숫자는 제거하고, 하나만 남긴다.
# 이 때 순서자체는 유지를 해야하는거죠.
"""
arr = [1, 1, 3, 3, 0, 1, 1]
1 3 0 1
배열에서 나오는 연속적인 숫자는 제거하고, 남은 수들만 리턴을 하는 문제.
stack = []
스택에 관련 값이 있는지를 확인해서, 있으면 넘기고, 없으면 넣는.
"""
def solution(arr):
    answer = [arr[0]] 
    # [1, 1, 3, 3, 0, 1, 1]
    # [1, 3, 0, 1]
    
    for num in arr: 
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
            
    return answer
    
    
        
    
            