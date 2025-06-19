def solution(n, words):
    answer = []
    sets = set()
    sets.add(words[0])
    
    for i in range(1, len(words)):
        print(i, words[i], sets)
        if words[i][0] != words[i-1][-1] or words[i] in sets:
            return [i % n + 1,i // n + 1]
        else:
            sets.add(words[i])
    
    return [0, 0]
        
            