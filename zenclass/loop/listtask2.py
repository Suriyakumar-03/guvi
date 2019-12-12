#program to check the value by comparing its modolus number
a=[]
b=[]

for i in range(0,3):
 list1=int(input("enter the values in list a:"))
 list2=int(input("enter the values in list b:"))
 a.append(list1)
 b.append(list2)
print(a)
print(b)

for j in range(0,len(a)):
 for k in range(0,j+1):
  if(a[j]==b[k]):
   print("it has same value in both list in required location")
  else:
   print("it doesn't value in both list")
    
