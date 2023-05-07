#121==121 then palidrome else not

n=121
temp=n
rev=0

while temp>0:
	rem=temp%10
	rev=(rev*10)+rem
	temp=temp//10
print(f"Reverse of {n} is {rev}")

if n==rev:
	print("Palindrome")
else:
	print("Not")