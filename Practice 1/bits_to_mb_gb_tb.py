bits = int(input("Enter number of bits : "))
byts = bits/8
kb = byts/1024
mb = kb/1024
gb = mb/1024
tb = gb/1024

print(f"{bits} is {byts} Byts, {kb} kb, {mb} mb, {gb} gb, {tb} tb")
