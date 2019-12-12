a=int(input("enter the number:"))
x=0
y=1
z=[]
for i in range(0,a):
 temp=0
 temp=temp+x
 z.append(temp)
 c=x+y
 x=y
 y=c
print(z)
