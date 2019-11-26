#program to find out sum of numbers
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))

if(a>b):
 print("a is greater")
 if(a<d):
  x=(a+c)
  print(x)
 else:
  print("a is less than d")

elif(b>a):
 print(" b is the greater number")
 if(b>d):
  y=(b+c)
  print(y)

elif(a==b):
 print("a is equal to b")
 if(c==d):
  v=(a+b)
  print(v)
 else:
  t=(c+d)
  print(t)

else:
 print("no number")
