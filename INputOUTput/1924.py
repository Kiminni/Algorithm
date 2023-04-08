M, D = map(int, input().split())
monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

sum = 0
i = 0
while (i < M - 1):
    if (M != 1):
        sum += monthList[i]
        i += 1
    else:
        break
sum += D

print(dayList[sum % 7])

'''
x, y=map(int,input().split())
M=[31,28,31,30,31,30,31,31,30,31,30,31]
D=[ 'SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

T=0
for i in range(x-1): #1월은 y로 알 수 있으니
    T+=M[i] 

T=T+y 
print(D[T%7])
'''
