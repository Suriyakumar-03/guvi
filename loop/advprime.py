#check the number which is equal to addition of two numbers from the list
n=int(input("enter the number:"))
list=[]
for i in range(3,n):
 for j in range(2,i):
    if(i%j==0):
      break
 else:
  list.append(i)
print(list)

for i in range(0,len(list)):
 for j in range(i,len(list)):
  if(list[i]+list[j]==n):
   print(list[i],list[j])
   break
 
