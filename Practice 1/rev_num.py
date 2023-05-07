n=123

l1=[]

while n!=0:
	rem=n//10
	n=n%10
	l1.append(n)
	n-=1

for x in l1:
	print(x,end="")
