# numbers라는 배열이 주어집니다.
# 여기서 서로 다른 인덱스에 있는 모든 수를 배열에 담습니다.
# 그 후에 오름차순으로 리턴을 하는 문제입니다.

# 그럼 여기서 시간복잡도 같은 경우는, 아무래도 반복문 2번을 돌아야 하니, O(n^2)이 될거라고 생각합니다.
# 이 친구는 반복문을 2번 돌텐데, 이 때 처음에는 
# [2 1 3 4 1]
# [2 3 4 5 6 7]
# [4 5 6 7 8 9 3 4 5 8...]
# 이미 그 값이 안에 있다면 넣지 않는 로직을 추가
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer))