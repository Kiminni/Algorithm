def solution(arr):
    stk = []
    for i in range(len(arr)):
        
        if stk != [] and stk[-1] == arr[i]:
            stk.pop(-1)
        else:
            stk.append(arr[i])
    
    if stk == []:
        return [-1]
    return stk

#     stk = []
#     for i in range(len(arr)):
#         if stk and stk[-1] == arr[i]:
#             stk.pop()
#         else:
#             stk.append(arr[i])

#     return stk or [-1]