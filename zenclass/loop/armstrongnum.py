#check whether the number is armstrong number is or not 
a=int(input("enter the number:"))
b=int(input("enter the number:"))
count=0
temp=b
x=0
for i in range(0,a):
 count+=1
if(count==3):
 for j in range(0,a):
  c=temp%10
  d=c**count
  temp=temp//10
  x=x+d
 if(x==b):
  print("it is the armstrong number")
else:
 print("it is the armstrong number")
 
