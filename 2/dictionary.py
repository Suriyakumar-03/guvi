#by using clear in dictinary method
mobile={"mobile":"iphone","model":"iphone6s"}
mobile.clear()
print(mobile)

#by using copy method
x={"guvi","god"}
z=x.copy()
print(z)

#by using fromkeys method
r=('guvi','zoho')
y=0
a = dict.fromkeys(r,y)
print(a)

#by using get method
a={"mobile":"iphone","model":"iphone6s"}
b=a.get("mobile")
print(b)

#by using item method 
o={"mobile":"iphone","model":"iphone6s"}
p=o.items()
print(p)

#by using keys method
r={"mobile":"iphone","model":"iphone6s"}
q=a.keys()
print(q)

#by using pop method
i={"mobile":"iphone","model":"iphone6s"}
j=i.pop("mobile")
print(j)

#by using popitem method
i={"mobile":"iphone","model":"iphone6s"}
j=i.popitem()
print(j)

#by using setdefult method
l={"mobile":"iphone","model":"iphone6s"}
m=i.setdefault("mobile","samsung")
print(m)

#by using update method
g={"laptop":"dell","gen":"i7"}
g.update({"memory":"1tb"})
print(g)

#by using pop method
dic={"mobile":"iphone","model":"iphone6s"}
w=dic.values()
print(w)