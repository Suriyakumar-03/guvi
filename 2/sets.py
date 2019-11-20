#using different command in set methods

#by using ADD method
hero={"ajith","kamal","vijay"}
hero.add("rajini")
print(hero)

#by using CLEAR method
a={"ajith","kamal","vijay"}
a.clear()
print(a)

#by using COPY method
b={"rajini","ajith","vijay"}
b.copy()
print(b)

#by using DIFFERENCE method
c={"rajini","ajith","vijay"}
d={"ajith","veeram","vaali"}
e=d.difference(c)
print(e)

#by using DIFFERENCE_UPDATE method
f={"rajini","ajith","vijay"}
g={"ajith","veeram","vaali"}
h=f.difference_update(g)
print(f)

#by using DISCARD method
h={"rajini","ajith","vijay"}
h.discard("vijay")
print(h)


#by using INTERSECTION method
i={"rajini","ajith","vijay"}
j={"ajith","veeram","vaali"}
i.intersection(j)
print(j)

#by using INTERSECTION_UPDATE method
k={"rajini","ajith","vijay"}
l={"ajith","veeram","vaali"}
l.intersection_update(k)
print(l)

#by using isdisjoint method
x={"guvi","zoho","zolo"}
y={"microsoft","ibm","cts"}
z= x.isdisjoint(y)
print(z)

#by using issubset method
com={"ola","uber","bike"}
cop={"driver","guvi","ola","bike","uber"}
p=com.issubset(cop)
print(p)

#by using issuperset method
co={"driver","guvi","ola","bike","uber"}
cm={"ola","bike","uber"}
q=co.issuperset(cm)
print(q)

#by using pop method
op={"guvi","zoho","zolo"}
op.pop()
print(op)

#by using remove method
po={"guvi","zoho","zolo"}
po.remove("zolo")
print(po)

#by using symmetric difference method
pr={"driver","guvi","ola","bike","uber"}
ps={"ola","bike","uber"}
s=pr.symmetric_difference(ps)
print(s)

#by using symmetric difference update method
pi={"driver","guvi","ola","bike","uber"}
pk={"ola","bike","uber"}
pi.symmetric_difference_update(pk)
print(pi)

#by using union method
op={"ola","guvi"}
pq={"guvi","zoho"}
rs=op.union(pq)
print(rs)

#by using update method
ab={"ola","guvi"}
cd={"zolo","zoho"}
ab.update(cd)
print(ab)