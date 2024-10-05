marks =[94.4 , 87.5 , 95.2 , 66.4 , 45.1]
print("The list if marks are :",marks)
print(len(marks))

for x in range (len(marks)):
    print(marks[x])


# a list can have combination of various types of 
# data types within a single list , below is an examople of this

student=["Shivam" , "Jobless" , 24 , 78.9]
print(student)  
# list in python is mutable but String in python us immutable

student[0]=3
print(student)
print(student[0:3])

# we can do negative indexing begining from right most end of list
# -5 -4 -3 -2 -1 <- starting from this end

list = [4,3,1,2]
list2=[5,7,6,8]
# append function can add elemnts at the end of one list
list.append(7)

print(list)
 
list.sort()
print(list)

# sorting in descenfing order
list2.sort(reverse=True)
print(list2)


# Sorting of strings and character is also possible
list=["banana", "litchi" , "Apple"]
list.sort(reverse=True)
print(list)

list.reverse()
print(list)


list = [4,3,1,2]
list.insert(0,5)
# the above fucntion insert actually adds the element at the given index
print(list)



# remove and pop function for list

print(list)
list.append(6)
print(list)
list.remove(6)
print(list)
list.pop(0)
print(list)


# copy function in list
ll2=list.copy()
print(ll2)


li=[]
print(type(li))

tup=(1)
print(type(tup))
print(tup)
# here when we print the type of tup we get int becaue we are entering a single element
# in tup , there if we insert a coma after that  1 like 1, the 
# python will able to understand that its a tuple
 
tup=(2,2,4,5,6,7,1)
print(tup)

# two important method in tuple


# count method
print(tup.count(2))

# index method : work similar to that of the find method 
print(tup.index(5))
