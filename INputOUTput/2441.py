'''
n = int(input())
j = 0
for i in range(n+1, 1, -1):
    print(' '*j, end = '')
    print('*' * (i- 1))
    j+=1
'''

n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i), '*' * i)