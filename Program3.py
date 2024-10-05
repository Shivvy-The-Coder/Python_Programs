str = input("Enter a string")
print(str[0:len(str)])

print(str.find("o"))

str=str.replace("o","A")
#  this wwill replace all the occurence of 'o' with 'A'.
# this can also be used to replace the string with another strings

print(str)
print(str.find("o"))

print(str.count("my"))

# Write a program to input user first name and print its length

name = input("Enter the name ")
print(len(name))

str = input("Enter the string ")
print(str.count("$"))
