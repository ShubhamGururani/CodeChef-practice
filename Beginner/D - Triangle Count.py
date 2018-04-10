for i  in range(int(input())):
    x, y = map(int, input().split())
    a = x - y + 1
    if y > x:
        print("Case "+str(i+1)+": 0")
    else:
        print("Case "+str(i+1)+":",a*(a+1)//2)