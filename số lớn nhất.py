a=int(input("so a:"))
b=int(input("so b:"))
c=int(input("so c:"))
if a>=b and a>=c:
    max=a
elif b>=a and b>=c:
    max=b
else:
    max=c
print(max)