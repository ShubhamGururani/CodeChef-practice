n = int(input())
ar = [int(i) for i in input().split()]
even = 0
odd = 0
for item in ar:
	if item % 2 == 0:
		even += 1
	else:
		odd += 1
if even > odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")