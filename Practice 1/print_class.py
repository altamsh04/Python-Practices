class Employee:
	def getData(self,name,department,salary):
		self.name=name
		self.department=department
		self.salary=salary

	def putData(self):
		print("Name : ",self.name)
		print("Department : ",self.department)
		print("Salary : ",self.salary)

emp = Employee()
emp.getData("pqr","CO","12345")
emp.putData()