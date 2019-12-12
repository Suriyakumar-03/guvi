a=int(input("enter the number:"))
s=int(input("enter the number:"))
s=s-2
for i in range(1,a+1):
 if(i<=3):
  for j in range(0,i):
   print("* ",end="")
  print("\r")
for k in range(a,3,-1):
 for l in range(1,(s-1)):
  print(end=" ")
 s=s+1
 for m in range(3,k):
  print("*",end="")
 print("\r")


