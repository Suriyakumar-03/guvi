#program to find out username and password by accessing them using key dictionary
b=input("enter the name:")
c=input("enter the password:")
a={"username":b,"password":c}
if("suriya"==a["username"]):
 print("the same username is:",a["username"])
 if("suriya123"==a["password"]):
  print("the password is:",a["password"])
 else:
  print("it has incorrect username and password")
else:
 print("wrong user")
