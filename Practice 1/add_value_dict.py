d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400} 

sumof = {}

for k1,v1 in d1.items():
	for k2,v2 in d2.items():
		if k1==k2:
			ans=v1+v2
			sumof.update({k1:ans})

print(sumof)