a = int(input())
if a % 3 == 0 or (a % 3 == 1 and a % 2 != 0):
	print("yes")
else:
	print("no")