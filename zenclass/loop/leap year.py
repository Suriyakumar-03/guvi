a=int(input("enter the number:"))
b=int(input("enter the number:"))
for i in range(a,b+1):
 if(i%4==0):
  print("the leap year",i)
 else:
  print("it is not leap year",i)
