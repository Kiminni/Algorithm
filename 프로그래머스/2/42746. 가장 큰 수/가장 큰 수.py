"""
1. list 내부 타입 한 번에 변경 후 정렬 하여 리턴
"""
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x : x*3, reverse=True)
    return str(int(''.join(numbers)))
    