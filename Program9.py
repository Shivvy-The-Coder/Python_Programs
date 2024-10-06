#   codes below here will belong to looping , jump statements etc


# while loop syntax and code is written below
# begining with 0
i=0
print(type(i))

while i<5:
    print("Hello")
    i+=1

print("final count value ", i)

# begining with 1
i=1
print(type(i))

while i<10000:
    print("Hello")
    i+=1

print("final count value ", i)


i=0
print(type(i))

while i<5:
    print(i)
    i+=1

print("final count value ", i)


# WAP print number from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

# WAP tp print number form 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

# Write a program to print all the first 10 multiples of that number
n=int(input("Enter the number "))
i=1
while(i<=10):
    print(n*i)
    i+=1

# Wap to Searxh for a number in tuple using loop
t=(1,2,3,4,5,6,7,8,9)
searching = int( input("Enter the numner your want tot search"))
i=0
while i <len(t):
    if t[i]==searching:
        print("found the number at ",i+1, " posiiton")
        break
    i+=1 