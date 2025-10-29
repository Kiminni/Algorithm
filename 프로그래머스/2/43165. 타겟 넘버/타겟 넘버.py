def solution(numbers, target):
    check = [0]
    for i in range(len(numbers)):
        for j in range(len(check)):
            check.append(check[j] - numbers[i])
            check[j] = check[j] + numbers[i]
            
    answer = check.count(target)
    return answer