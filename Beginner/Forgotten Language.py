for _ in range(int(input())):
	n,k=map(int, input().strip().split())
	w1=""
	ans=""
	w=input()
	w=w.strip().split()
	for _ in range(k):
		w1=w1+input()+" "		
	w1=w1.strip().split()
	for x in range(len(w)):
		if w[x] in w1:
			ans=ans+"YES"+" "
		else:
			ans=ans+"NO"+" "
	print(ans)		