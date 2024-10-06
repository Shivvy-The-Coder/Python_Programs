nums =[1,2,3,4,5]

for val in nums:
    print(val)

veggies =["potato" , "brinjal"  , "ladyfinger" , "cucumber"]
for i in veggies:
    print(i)

tup = (1,2,3,4,5,6,7)
for i in tup:
    print(i)

str="ShivamKumarDas"
for i in str:
    print(i)
else:
    print("End of string")


# else with for loops  comes handy when we use break in the loop 


# create a list of squares of elments 1 to 10
list=[]

for i in range(1,11):
    list.append(i**2)
    i+=1
print(list)

tup=tuple(list)
for i in tup:
    print(i)
    i+=1

search =int(input("Enter the number you want to search in tuple"))
for i in tup:
    if i==search:
        print("Number found")
        break
else:
    print("Completed")
    

# types of range in python for using for loop 
for i in range (5):
    print(i)
#  in above code we have only set the stop value at whcih the forloop should stop
# end value is never inclusive in range

# we can also set the start value and end value in range function
for i in range (1,5):
    print(i)
    
# in above code we have wrote the start value and end value , oif we want the end calue to be inclusive in that case we
# have to add +1  to the end value in range function
for i in range (1,5+1):
    print(i)

# in above codes we can see that increment is done by 1 
# but we can also hvae an increment by  2 or 3 or any number we want

for i in range(0,10,2):
    print(i)

# if we dont want the increment value here we can do it normal ways
x=0
for i in range (0,5):
    x+=2
    print(x)
    
# WAP to print number from 1 to 100
for i in range (100):
    print(i)

# WAP to print number from 100 to 1
for i in range (100,0,-1):
    print(i)

# WAP to print the first 10 multiples of Number n
n=int(input("Enter the Number")) 
for i  in range (1,11):
    print(n*i)


# pass statement in python is used to simply null a stetment in such a way that we 
# we will write that perticular set code after sometime
for i in range (10):
    pass

print("pass worked")



# sum of first n number using while loop
n=int(input("Enter the number"))
sum=0
while n!=0:
    sum+=n
    n-=1
print("Sum of first N Numbers is ", sum )


# Wap to find the factorial of first n nuber using for loop
inp=int(input("Enter the number"))
fact=1
for i in range(1,inp+1):
    fact*=i

print("factorial of given number is ",fact)