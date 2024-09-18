def solution(k, dungeons):
    answer = 0
    for dungeon in dungeons:
        if k >= dungeon[1] and k >= dungeon[0]:
            k -= dungeon[1]
            answer += 1
    return answer