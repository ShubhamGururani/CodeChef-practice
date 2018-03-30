n1, n2, n3 = map(int,input().split())
ar = set()
ar2 = []
for i in range(n1+n2+n3):
	x = int(input())
	len1 = len(ar)
	ar.add(x)
	if len(ar)==len1:
		ar2.append(x)
ar2 = sorted(set(ar2))
print(len(ar2))
for item in ar2:
	print(item)