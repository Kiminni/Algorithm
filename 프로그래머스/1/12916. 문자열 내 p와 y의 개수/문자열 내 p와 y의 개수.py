"""
문자열 s가 주어집니다. p와 y의 개수를 출력해서, 같으면 t / 다르면 f를 반환하는 문제
모두 하나도 없다면, 항상 true 반환합니다.
개수 비교시, 대소문자는 구별하지 않음.

1. 문자를 다 소문자로 만들고
2. 반복문을 돌면서 p와 y를 구합니다.
3. 그리고 결과를 출력

"""
def solution(s):
    ans_p, ans_y = 0, 0
    for string in s.lower():
        if string == "p":
            ans_p += 1
        elif string == "y":
            ans_y += 1
    # 이 상태에서는 개수가 항상 없더라도, 결국엔 다 0으로 처리가 되기 때문에 무조건 true
    return ans_p == ans_y
            

    