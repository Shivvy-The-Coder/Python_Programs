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