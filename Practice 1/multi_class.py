#multiple inheritance

class emp_name:
	def get_name(self,name):
		self.name=name

class emp_dep:
	def get_dep(self,dep):
		self.dep=dep
		super().get_name("pqr")

class emp_sal(emp_dep,emp_name):
	def get_sal(self,sal):
		self.sal=sal
		super().get_dep("CO")

	def putData(self):
		print("Name : ",self.name)
		print("Department : ",self.dep)
		print("Salary : ",self.sal)

a1 = emp_sal()
a1.get_sal(1234567)
a1.putData()
