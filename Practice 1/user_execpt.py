n1=int(input("Enter n1 : "))
n2=int(input("Enter n2 : "))

try:
	res = n1/n2
	print(res)
except Exception:
	print("ZeroDivisionException")
finally:
	print("Finally executed")
