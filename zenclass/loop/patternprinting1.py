#pyramid pattern printing
a=int(input("enter the number:"))
s=a-1
for i in range(0,a):
 for j in range(0,s):
  print(end=" ")
 s=s-1
 for k in range(0,i+1):
  print("* ",end="")
 print("\r")



