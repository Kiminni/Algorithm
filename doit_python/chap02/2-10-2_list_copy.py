x = [[1,2,3], [4,5,6]]

y = x.copy()

print(x)
print(y)

x[0][1] = 9
print(x) 
print(y) # 얕은 복사 > 참조하는 곳까지 같음

