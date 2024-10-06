# here we will do some basic recursion problems 

# Wap to print the number in decreasing number
def prin(n):
    if n==0:
        return
    print(n)
    prin(n-1)

prin(5)

# Wap to print the number in Increasing number
def prin(n):
    if n==0:
        return
    prin(n-1)
    print(n)
    

prin(5)

# fcatorial program for recursion
def factorial(n):
    if(n==0):
        return 1
    a=factorial(n-1) *n
    return a

print(factorial(5))

# recursie fucntion to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    s=sum(n-1)+n
    return s

a=sum(3)
print(a)

# WA recursive function to print all the elements preset inside the list

def prili(ll, i):
    if i==len(ll):
        return 
    prili(ll, i+1)
    print(ll[i])


prili([1,2,3,4,5], 0)


# returning multiple values in function  using tuple

def printfirstThree(n):
    return  (n,n+1,n+2)

a,b,c=printfirstThree(5)
print(a)  # output: 5 6 7


def subtract_and_multiply (a, b):
    return a-b ,  a*b

sub,mul = subtract_and_multiply(5,3)
print(sub,mul)

# above we can see that there are ,multiple returned value we are storin them in the form of tuples
# we can also use dictionary to return multiple values from a function

def subtract_and_multiply (a, b):
    return[ a-b ,  a*b]

s = subtract_and_multiply(5,3)
print(s[0],s[1])


# we can e=also return tyhe data inform of dicitonary

def subtract_and_multiply (a, b):
    return {"sub ":a-b ,"mul" :a*b}

s = subtract_and_multiply(5,3)
print(s["mul"],s["sub "]) 