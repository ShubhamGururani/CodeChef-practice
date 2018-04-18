def sumDigit(x):
    sumD = 0
    while x != 0:
    	sumD = sumD + x % 10
    	x = x // 10
    return sumD
num = int(input())  
times = 0
for i in range(num - 100 , num + 1):
	if i+sumDigit(i)+sumDigit(sumDigit(i))== num :
		times += 1
print(times)