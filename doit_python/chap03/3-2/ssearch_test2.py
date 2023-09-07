# seq_search() 함수를 이용해 특정 인덱스 검색하기

from ssearch_while import seq_search 

t = (4, 7, 5.6, 2, 2.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
print(f'{s}에서 r의 인덱스는 {seq_search(s, "r")}입니다.')
print(f'{a}에서 5.6의 인덱스는 {seq_search(a, "AAC")}입니다.')

