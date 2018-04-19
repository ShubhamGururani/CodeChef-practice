dict={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
n = int(input())
for i in range(0,n):
    sum = 0
    q = input()
    if len(q)<=1:
        sum = 0
    else:
        for j in range(0, len(q) - 1):
            if dict[q[j]] > dict[q[j + 1]]:
                x = 26 - (dict[q[j]] - dict[q[j + 1]])
                sum += x
            else:
                x = (dict[q[j + 1]]-dict[q[j]])
                sum += x
    y = 1 + len(q) + sum
    if y <= len(q) * 11:
        print("YES")
    else:
        print("NO")