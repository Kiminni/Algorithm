from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    def can_convert(word1, word2):
        count = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                count += 1
            if count > 1:
                return False
        return count == 1
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while deque:
        c, s = queue.popleft()
        if c == target:
            return s
        
        for word in words:
            if word not in visited and can_convert(c, word):
                visited.add(word)
                queue.append([word, s + 1])
    return 0
    