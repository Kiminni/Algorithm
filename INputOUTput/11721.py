S = input()
for i in range(0, len(S), 10):  # 시작값, 종료값, STEP(10개씩)
    print(S[i:i+10])  # S[시작값, 종료값]


'''
for i in range(len(S)):
    i = i + 1
    print(S[i-1], end = '')
    if(i % 10 == 0):
        print()
'''
