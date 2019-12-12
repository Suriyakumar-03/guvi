#program to sum all the numbers by getting the modulous number from user
a=[]
n=int(input("enter the length of list:"))
k=int(input("enter the number:"))
x=0
for i in range(n):
 list=int(input("enter the values:"))
 a.append(list)
 if(i<=k):
  x=x+a[i]
print(x)

  
