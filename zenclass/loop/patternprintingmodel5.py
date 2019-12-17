#pattern printing model:6
a=int(input("enter the number:"))
s=int(input("enter the number:"))
s=s-2
for i in range(1,a+1):
 for l in range(s,2,-1):
  print(end=" ")
 s=s-1
 if(i<=2):
  for j in range(0,i):
   print(" *",end="")
  print("\r")
 if(i==3):
  print("* "*i,end="")
  print("\r")
for k in range(a,3,-1):
 for l in range(s,-1):
  print(end=" ")
 s=s-1
 for m in range(3,k):
  print("* ",end="")
 print("\r")

