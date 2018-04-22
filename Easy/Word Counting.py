from collections import Counter
from math import factorial
num = 10 ** 9 + 7
for _ in range(int(input())):
	string = input()
	count = Counter(string)
	f = factorial(len(string))
	x = 1
	for i in count.values():
		if i > 1:
			x *= factorial(i)
	print((f // x) % num)