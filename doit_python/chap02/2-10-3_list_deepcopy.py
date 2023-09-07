import copy

x = [[1,2,3], [4,5,6]]

y = copy.deepcopy(x) # 

print(f'before x = {x}')
print(f'before y = {y}')

x[0][1] = 9 
print(f'after x = {x}')
print(f'after y = {y}')

# 얕은 복사 - 참조 값만 복사
# 깊은 복사 - 참조하는 객체 자체를 복사