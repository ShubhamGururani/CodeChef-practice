def Perfect(number):
	number = number ** 0.5
	if number == int(number):
		return True
	return False
a, b = map(int,input().split())
num = 0
for i in range(1,a+1):
	for j in range(1, b+1):
		if Perfect((i**2) + j):
			num += 1
print(num)