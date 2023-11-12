def solution(numbers):
    answer = ''
    tmp = ''
    eng_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(numbers)):
        tmp += numbers[i]
        if len(tmp) >= 3:
            for j in range(len(eng_list)):
                if tmp == eng_list[j]:
                    answer += num_list[j]
                    tmp = ''
                    break
            

    return int(answer)