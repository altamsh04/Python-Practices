# 0		1		1		2		3		5
# pre 	cur 

n = int(input("Enter n :"))

pre = 0
cur = 1
print(pre,' ',end='')
print(cur,' ',end='')

while n!=0:
	fib=pre+cur
	pre=cur
	cur=fib
	print(fib,' ',end='')
	n-=1
