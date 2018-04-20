for _ in range(int(input())):
    num = int(input())
    ar = list(map(int,input().split()))
    for i in range(0,num-2):
        if ar[i] == ar[i+1] == ar[i+2]:
            print("Yes")
            break
    else:
        print("No")