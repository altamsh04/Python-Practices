class stud_name:
	def getData1(self,name):
		self.name=name

class stud_roll(stud_name):
	def getData2(self,roll):
		self.roll=roll
		super().getData1("altamsh")

	def putData(self):
		print("Name : ",self.name)
		print("Roll : ",self.roll)

sn = stud_roll()
sn.getData2(2)
sn.putData()