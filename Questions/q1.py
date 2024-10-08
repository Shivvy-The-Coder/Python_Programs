s="django"

print(s[0:1])
print(s[len(s)-1])
print(s[0:len(s)-2])
print(s[1:4])
print(s[4:6])

str=""
for i in s:
    str=i+str
print(str)

x=s[::-1]
print(x) 

l=[37,1,[1,4,'hello']]
print(l)
l[2][2]="good bye"
print(l)

d1={"simple_key":'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1.get("simple_key"))
print(d2.get('k1').get('k2'))
print(d3.get('k1')[0].get('nest_key')[1][0])



mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,3]
s=set()
for i in mylist:
    s.add(i)

print(len(s))