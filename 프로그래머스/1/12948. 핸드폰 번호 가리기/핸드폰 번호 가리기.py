def solution(phone_number):
    length = len(phone_number)
    answer = ''
    for i in phone_number:
        if length - len(answer) > 4:
            answer += "*"
    return answer + phone_number[len(phone_number) - 4:]