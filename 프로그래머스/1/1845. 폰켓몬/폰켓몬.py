def solution(nums):
    answer = []

    for num in nums:
        if len(answer) >= len(nums) / 2:
            break
        if num not in answer:
            answer.append(num)
    
    return len(answer)