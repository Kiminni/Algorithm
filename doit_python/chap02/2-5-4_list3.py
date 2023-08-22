# 리스트의 모든 원소 스캔하기 (1부터 시작)

x = ['John', 'George', 'paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번쨰 = {name}')