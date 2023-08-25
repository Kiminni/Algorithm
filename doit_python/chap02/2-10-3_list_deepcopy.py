import copy

x = [[1,2,3], [4,5,6]]

y = copy.deepcopy(x)

print(f'before x = {x}')
print(f'before y = {y}')

x[0][1] = 9
print(f'after x = {x}')
print(f'after y = {y}')
