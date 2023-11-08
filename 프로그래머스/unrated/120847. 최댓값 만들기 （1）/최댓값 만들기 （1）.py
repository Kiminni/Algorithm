def solution(numbers):
    answer = 0
    num1 = max(numbers)
    numbers.pop(numbers.index(max(numbers)))
    num2 = max(numbers)
    return num1 * num2