d1 = {'a':10, 'b':20, 'c':30}

high = None
for k1,v1 in d1.items():
    if high is None or v1 > high:
        high = v1

print("Highest value in dictionary:", high)
