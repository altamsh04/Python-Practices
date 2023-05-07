str = input("Enter String : ")
l = 0
u = 0

def fun(str):
    global l, u
    
    for s1 in str:
        if s1.islower():
            l += 1
        elif s1.isupper():
            u += 1

fun(str)
print("Lower value : ", l)
print("Upper value : ", u)
