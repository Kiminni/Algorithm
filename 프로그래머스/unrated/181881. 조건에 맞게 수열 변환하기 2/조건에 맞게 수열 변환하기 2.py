# import copy
# def solution(arr):
#     temp = []
    
#     answer = 0
#     flag = 1
#     i = 0
    
#     for num in arr:
#         temp.append(num)
#     while(flag == 1):
#         if temp[i] >= 50 and temp[i] % 2 == 0 :
#             temp[i] //= 2

        
#         elif temp[i] < 50 and temp[i] % 2 == 1:
#             if temp[i] * 2 + 1 <= 100:
#                 temp[i] = temp[i] * 2 + 1
                
        
#         i += 1
#         if temp == arr and i == len(arr): 
#             flag = 0

#         elif temp != arr and i == len(arr) :   
#             answer += 1
#             arr = copy.deepcopy(temp)
#             i = 0
        
#     return answer

def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer