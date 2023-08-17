# +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input("몇 개를 출력할까요? "))

for _ in range(n//2): # 언더스코어 -> 무시하고 싶은 값을 출력할 때 (index가 필요하지 않음)
#for _ in range(1, n//2 + 1): # count 0 -> 1로 변경
    print('+-', end = "") # +-를 n//2 개의 출력


if n%2:
    print('+',end = "") # n이 홀수면 한 번 더 마지막 + 출력
print()