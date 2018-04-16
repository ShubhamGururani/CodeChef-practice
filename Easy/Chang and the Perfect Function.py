from math import sqrt
a, b = map(int, input().split())
num = 0
for i in range(1, a):
    num += int(sqrt((i * i + b)) - i)
print(num)