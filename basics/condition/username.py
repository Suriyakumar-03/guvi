#program to find suitable cars for username by using nested if conditon
username=input("enter the username:")
password=input("enter the password:")
cars=input("enter the car name:")
car=["audi","bmw","benz"]

if(username=="suriya"):
 print("the username is:",username)
 if(password=="suriya"):
  print("the password is:",password)
  if(car[0]==cars):
   print("it is audi")
  elif(car[1]==cars):
   print("it is bmw car")
  else:
   print("it is benz car")

 else:
  print("the password is too weak")

elif(username=="hameesh_bro"):
 if(password=="hameesh"):
  print("it is for sepreate user")
  if(car[0]==cars):
    print("it is audi")
  elif(car[1]==cars):
    print("it is bmw car")
  else:
    print("it is benz car")
 else:
  print("the password is not assigned for username")

else:
 print("the username is incorrect")
