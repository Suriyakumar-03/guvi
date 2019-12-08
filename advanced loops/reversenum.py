a=int(input("enter the number:"))
b=int(input("enter the number:"))
rev_num=0
temp=b
for i in range(0,a):
 d=temp%10
 rev_num=rev_num*10+d
 temp=temp//10
print(rev_num)
 

