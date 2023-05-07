class PasswordException(Exception):
	def __init__(self):
		print("Password fail")
		super().__init__()

try:
	p = "123"
	if p=="123":
	 	print("Password successful")
	else:
		raise PasswordException()
finally:
	print("finally.......")
