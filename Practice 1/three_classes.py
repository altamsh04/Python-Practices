class Degree:
	def getDegree(self):
		print("I got a degree")

class Undergraduate(Degree):
	def getUndergraduate(self):
		print("I am an Undergraduate")

class Postgraduate(Degree):
	def getPostgraduate(self):
		print("I am a Postgraduate")

ug = Undergraduate()
pg = Postgraduate()
dg = Degree()

dg.getDegree()
ug.getUndergraduate()
pg.getPostgraduate()