n=6 #6*5*4*3*2*1

facto=1

while n!=0:
	rem=n//10
	n=n%10
	facto=facto*n
	n-=1
print(f"Factorial of 6 is {facto}")