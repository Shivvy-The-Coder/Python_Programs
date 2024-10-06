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

dic={"name ":"Shivam",
     "surname":"Das",
     "Marks":{"Maths":90,"English":96,"Physics":98},
     "Age ":24}

for i in dic:
    print(type(i),i)
    

