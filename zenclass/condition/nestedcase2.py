#program to find suitable cars 
a="ford"
b=input("enter the car name:")
c=input("enter the car name:")
d=input("enter the car name:")

if(a==b):
 print("it is used for taxi")
 if(a==d):
  print("it has a same engine")
  print(d)
 else:
  print("it doesn't suit for taxi")

elif(a==c):
 print(" c is used for f1")
else:
 print("it is not a car")
