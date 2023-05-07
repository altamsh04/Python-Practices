n=123 #6*5*4*3*2*1

sumof=0

while n!=0:
	rem=n//10
	n=n%10
	sumof=sumof+n
	n-=1
print(sumof)