l1 = [10,20,50,40,30]
l2 = [60,50,100,80,30]

c = []

for x in l1:
	for y in l2:
		if x==y:
			c.append(x)

print(c)