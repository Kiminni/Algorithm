n = int(input())

for i in range(1, n+1):
    print('*' *(i) + ' '*(n-i) + ' '*(n-i) + '*'*i)

for j in range(1,n):
    print('*'*(n-j) + ' '*(j) + ' '*(j)+ '*' * (n-j))