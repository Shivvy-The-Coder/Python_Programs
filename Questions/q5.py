# herre wwe will work on inheritance and special methos
#  INheritance is a way of making a new classes with the help of previosly build class, this reduces the rewritting of code 
#  as we use previosly written code , the class which has been used to crate the new class isn called parent class or base class
# whereras the new class is called child class or derived class

class Animal():
    def __init__(slef):
        print("Animal created")
    def Whoami(slef):
        print("I am an animal")
    def eat(self):
        print("I am eating")

mya=Animal()
mya.eat()




#  here we wll use previously defined Animal calss and acces all the functionalities that is beingr provided by ANimal class

class Dog(Animal): 
    def __init__(self):
        # Animal.__init__(self) 
        print('DOG Created')
    def bark(slef):
        print("Wooof Woof")
    def Whoami(slef):
       print("Dog Eating")


mydog=Dog()
mydog.eat()
mydog.Whoami()
mydog.bark()


# special methods 

mylist=[1,2,3]
print(mylist)


class Book():
    def __init__(self,title , author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def __str__(self):
        return "title:{},Author:{}, Pages:{}".format(self.title , self.author , self.pages)
     
    def __len__(self):
        return self.pages
         
    def __del__(self):
        print("Book is deleted")
b=Book("Shiva","hose",123 )
print(b)

print(len(b))
del b
