def solution(arr):
    answer = [[]]
    for i in range(len(arr)):
        while len(arr[i]) < len(arr):
            arr[i].append(0)
            
        while len(arr) < len(arr[i]):
            arr.append([0]*len(arr[i]))
            
    return arr