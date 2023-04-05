while(1):
    try: #개수가 정해져있지 않으니 
        A,B = map(int,input().split())
        print(A+B)
    except: #아니면 break를 걸어야
        break
