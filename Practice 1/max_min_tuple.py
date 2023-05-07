t1 = (0,1,2,3,4,5,20,6,7,8,9,10)

# print(max(t1))
# print(min(t1))

maxof = None
minof = None

for x in t1:
	if maxof is None or maxof < x:
		maxof = x

for y in t1:
	if minof is None or minof > y:
		minof = y

print("Maximum : ",maxof)		
print("Minimum : ",minof)