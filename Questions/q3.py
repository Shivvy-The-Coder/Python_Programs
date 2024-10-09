name ="this is a global variable"

def nameit():
    name ="Shivam"

    def answer():
        print("Hello welcoe  to my channel",name)
    answer()
nameit()
# this will print hello welcome to my chanel, shivam becasue shivam is assigned  name variable to this fucntion
# suppose we comment out the name variable in nameit() then it will printn the gloabal varibale for output

nameit()


print(name)


# here we can see that we have declared len =5 where as len is builtin fcuntion that we are using
len=10
print(len)



# we shoould avoid changing any global data directly it increases the risk of namespacing 
#  therer we can us ethe below methidi which mnimizes the risk of these factors

#  we can use return to change any gobal fata we want 
x=1000
def change ():
    return 100

print("before calling the ficntion change ",x)
x=change()
print("After calling the function change",x)


