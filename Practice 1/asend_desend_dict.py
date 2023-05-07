my_dict = {'a': 23, 'b': 45, 'c': 12, 'd': 67}

nd1 = sorted(my_dict.items(),key=lambda x:x[1])
nd2 = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)

print(nd1)
print(nd2)