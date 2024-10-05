marks = int(input("Enter the marks you got "))

if(marks >=90):
    print("A")
elif(marks<90 and marks>=80):
    print("B")
elif(marks<80 and marks>=70):
    print("B")
else:
    print("D")    


# nesting if statement
age = 34
if(age>18):
    if(age>80):
        print("cannot Drive")
    else :
        print("can Drive")
else:
    print("cannot Drive")


#WAP check a number entered by user is even or odd

num =int(input("ENter a number to be checked "))
if(num%2==0):
    print("num is a even number")
else:
    print("num is a odd number ")
    

# WAP to find the  largest of three numbers

num1 =int(input("ENter the 1st number"))
num2 =int(input("ENter the 2nd number"))
num3 =int(input("ENter the 3rd number "))

if(num1 > num2 and num1 >num3):
    print(num1," is Greatest")
elif(num2 > num1 and num2 >num3):
    print(num2," is Greatest")
else:
    print(num3," is Greatest")


# WAP program to check wether a number is multiple of 7 or not
num = int (input("Enter the number to be checked "))
if(num%7==0):
    print(num," is a multiple of 7")
else:
    print(num," is not a multiple of 7")