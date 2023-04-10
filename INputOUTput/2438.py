
'''
N = int(input())
i = 0
j = 0
while(i < N):
    i += 1
    j = 0
    if(i != 1):
        print()
    while(j<i):
        print('*', end = '')
        j += 1
'''

n = int(input())
for i in range(1, n+1) : 
  print(' '*(n - i), end = '')
  print('*' * i)