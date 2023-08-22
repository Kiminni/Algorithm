# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

import_max = __import__("2-2_max")

t = (4,7,5.6,2,3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {import_max.max_of(t)}입니다.')
print(f'{s}의 최댓값은 {import_max.max_of(s)}입니다.')
print(f'{a}의 최댓값은 {import_max.max_of(a)}입니다.')
