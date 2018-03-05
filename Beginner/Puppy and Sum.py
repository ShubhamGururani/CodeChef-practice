def sum(n):
	return (n * (n + 1))/2
 
for _ in range(int(input())):
	time,x = list(map(int, input().split()))
	
	for __ in range(time):
		x = sum(x)
	print(int(x))  
