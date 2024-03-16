def solution(s):
    answer = []
    word_dict = {}
    for idx, word in enumerate(list(s)):
        if word not in word_dict:
            word_dict[word] = idx
            answer.append(-1)
            
        else :
            answer.append(idx - word_dict[word])
            word_dict[word] = idx
            
    return answer