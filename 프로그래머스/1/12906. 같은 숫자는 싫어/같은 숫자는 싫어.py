def solution(arr):
    ans = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        ans.append(arr[i])
    
    return ans
            
        
            
    