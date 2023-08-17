'''
N = int(input())
for i in range(N, 0, -1):
    print(i)
'''

print("\n".join(map(str, range(int(input()), 0, -1))))
