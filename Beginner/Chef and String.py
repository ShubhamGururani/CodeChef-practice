s = list(input())
c=h=e=f=0
for char in s:
	if char == "C":c+=1
	if char == "H" and c>0:
		h+=1
		c-=1
	if char == "E" and h>0:
		e+=1
		h-=1
	if char == "F" and e>0:
		f+=1
		e-=1
print(f)