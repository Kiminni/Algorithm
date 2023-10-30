def solution(arr):
    ans = []
    
    for i in range(len(arr)):
        tmp = []
        for j in range(len(arr)):
            tmp.append(arr[j][i])
        ans.append(tmp)
    
    if ans == arr:
        return 1

    return 0