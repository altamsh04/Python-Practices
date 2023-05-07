l1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

s1 = set()

for x in l1:
	for k1,v1 in x.items():
		if k1 not in s1:
			s1.add(v1)
print(s1)