info ={
    "key" :"value",
    "name":"Shivam",
    "learning": "Python",
    "subjects": ["maths","Python","Aptitude"]
}

print(info)
print(len(info))
print(info["key"])
print(info.__contains__("key"))
 
for i in info:
    print(i)


info["surname"]="das"

for i in info:
    print(i)


# we can create a null dictionary by using a {}

dic={}
print(dic)
print(type(dic))


nm=int(input("Ener the numbr of values you want to input"))
for i in range (0,nm):
    key=input("Enter the key")
    value=input("Enter the value")
    dic[key]=value

print(dic)


# how to use nested dictionary in python

dic={"name":"Shivam",
     "surname":"Das",
     "Marks":{"Maths":90,"English":96,"Physics":98},
     "Age ":24}

 
print(dic["Marks"])
print(dic["Marks"]["Physics"])

#  this will print all the key's present in the dictionary in form of tuple by type casting
print(tuple(dic.keys()))
#  this will print all the key's present in the dictionary in form of list by type casting
print(list(dic.keys()))

#  this will print all the value's present in the dictionary in form of set by type casting
print(tuple(dic.values()))
# thus will print all the  value's present in the dictionary in form of list by type casting
print(list(dic.values()))

print(dic["Marks"])


# accesing the key value pairs in form  of tuple
print(list(dic.items()))
# above we can see output in the form of 
# [('name ', 'Shivam'), ('surname', 'Das'), ('Marks', {'Maths': 90, 'English': 96, 'Physics': 98}), ('Age ', 24)]
# ,as  they are written inside of the ()  they are in the form of tuple.


# how to access the tuples stored index wise
# first store the dictionary in a tuple
dict = tuple(dic)


dic={"name":"Shivam",
     "surname":"Das",
     "Marks":{"Maths":90,"English":96,"Physics":98},
     "Age ":24}
# we can access the values present int= the dictionary via 2 ways

print(dic["name"])
print(dic.get("name"))

#  aftrw the error gets encountred the upcomming line sin code wont get executed
#  therer forer it will create a huge mess if we deploy the samw code supporse we are doing ir for the backend
# therefore we will use .get() as it handels the exception and return none if the perticular key doesnto exist in the 
# dictionary, as well as executes the upcomminh line without any problem.

dic["city"]="delhi"
print(dic) 

# using update function to add new key value pairs in already exisiting dictionary
dic.update({"State":"Jharkhand"})
print(dic)

# adding a dictionary inside another dictionary using update method
Address={"State":"Jharkhand",
       "pincode":"834010",
       "stret":"13th Backstreet WheelTown Road"}

dic.update(Address)
print(dic)

print(dic.keys())



# sets in pythom
collections={}
print(type(collections))

collections={1,2,3,4}
print(type(collections))

# defining an empty set is similar to defining an wempty dictionary
# set is an unordered , and duplicate values in set is not allowed

# how to define an empty set 
collection=set()
# the above code will define an empty set 
print(collections)
collections.add(1)
collections.add(2)
collections.add(3)
collections.remove(1)
# collections.remove(7)
collections.add("Shivam")
print(collections)

# ll=["hellow" , "World " , "123"]
# collections.add(ll)

print(collections.pop())


# performing set operation in pyton

setA={1,2,3,4,5}
setB={2,3,4,5,6}
# union of two sets
print(setA.union(setB))
# intersection of two sets
print(setA.intersection(setB))