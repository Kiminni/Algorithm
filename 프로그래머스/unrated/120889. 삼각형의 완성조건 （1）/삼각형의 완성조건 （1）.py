def solution(sides):

    sides.sort(reverse=True)
    if sides[0] < sides[1] + sides[2]:
        return 1
    return 2