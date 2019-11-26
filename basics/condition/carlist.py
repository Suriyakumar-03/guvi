b=str(input("enter the name:"))
c=str(input("enter the password:"))
y=str(input("car type:"))
x=str(input("car model:"))
micro=["nano","kwid","baleno"]
suv=["xylo","xuv500","sumo"]
sedan=["verna","xcent","altis"]
a={"username":b,"password":c}
if("suriya"==a["username"]):
 print("the same username is:",a["username"])
 if("suriya123"==a["password"]):
  print("the password is:",a["password"])
  if(y == "micro"):
   print("the car type is micro")
   if(micro[0]==x):
    print("nano car is suitable for this user")
   elif(micro[1]==x):
    print("kwid is suitable car for this user")
   elif(micro[2]==x):
    print("baleno is suitable car for this user")
  elif(y =="suv"):
   print("the car type is suv")
   if(suv[0]==x):
    print("xylo is suitable car")
   elif(suv[1]==x):
    print("xuv500 is suitable car")
   elif(suv[2]==x):
    print("sumo is suitable car")
  elif(y =="sedan"):
   print(" the model is sedan")
   if(sedan[0]==x):
    print("it is verna car for the user")
   elif(sedan[0]==x):
    print("it is xcent model")
   else:
    print("it is altis model")
 else:
     print("it is incorrect user")
       
 
else:
  print("car is not in list of your expecation")
