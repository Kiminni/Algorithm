from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    def can_convert(word1, word2):
        count = 0
        for x, y in zip(word1, word2):
            if x != y:
                count += 1
            if count > 1:
                return False
        return count == 1
    
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        
        for word in words:
            if word not in visited and can_convert(current, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0