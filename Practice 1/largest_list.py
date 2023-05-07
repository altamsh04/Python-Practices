l1=[10,20,30,100,40,50]

# print(max(l1))
lar = None
for x in l1:
	if lar is None or lar < x:
		lar = x
print(lar)