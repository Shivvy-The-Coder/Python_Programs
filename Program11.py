# we write the function to remove the redundancy
def area(a,b):
    print(a*b)
    return a*b

area(10,5) 

a=area(9,6)

# we can create a function which does not take any parameter and return a value

def sum ():
    print(5*4)

sum()

# we can create a function which takes value but does not return any value

def sum (a,b):
    print(a+b)

sum(5,4)


# we can create a function which takes any parameter and return a value
def area(a,b):
    print(a*b)
    return a*b

area(10,5) 



# we can create a function which does not takes value and does not return any value

def print_hello():
    print("Hello")

print_hello()

# if a function is not returning anything and we try to store the function inside some variable in that case
# that vriable will have "none " 


# WAP to calculate and return the average of n numbers in, list
nums=[1,2,3]
def Average(nums):
    sum=0
    for i in nums:
        sum+=i
    print(sum)
    return sum/i

print(Average(nums))


# python have some built functions 
#  range() , print() , type() , len() etc


#  default paramerters
def cal_product(a=4,b=5):
    print(a*b)
    return a*b

cal_product(b=5)

# Write a fucntion to print the length of the list as parameter


def findlen(li):
    return len(li)

def printlist (li):
    for i in li:
        print(i,end=" ")

def finfact(n):
    fact=1
    while n!=0:
        fact*=n
        n-=1
    return fact

def USDtoINR(usd):
    return  usd*74.5



li=[1,2,4,5,6,2,3,5,6,8,11]

print(printlist(li))
print(finfact(5))
print(USDtoINR(5))
print(findlen(li))


cities = ["delhi" , "gurgaon" , "noida" , "pune" , "mumbai" , "chennai"]
heroes = ["thor" , "ironman" , "CAptain AMerica" , "Spiderman" , "Shaktiman"] 

print(findlen(cities))
print(findlen(heroes))

# WAF which will take a number as an input whcih will print odd if the number passed in parameter is odd
# else it should print even 

def evenOdd(n):
    if n%2!=0:
        print("odd")
    else:
        print("even")

evenOdd(5)

