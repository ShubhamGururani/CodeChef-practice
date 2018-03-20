for _ in range(int(input())):
	n=int(input())
	prob=set()
	for _ in range(n):
		prob.add(input())	
	valid=set(["cakewalk","simple","easy"])
	if prob.issuperset(valid) and ("easy-medium" in prob or "medium" in prob) and ("medium-hard" in prob or "hard" in prob):
		print("Yes")
	else:
		print("No")