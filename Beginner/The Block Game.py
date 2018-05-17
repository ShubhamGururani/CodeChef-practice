for i in range(int(input())):
    n = input()
    ar = list(n)
    ar.reverse()
    s = ""
    for i in ar:
        s += i
    if(s == n):
        print("wins")
    else:
        print("losses")