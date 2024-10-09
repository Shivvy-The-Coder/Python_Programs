# this python file will help us to learn object oriented programming
print(type([]))
print(type({}))
# above we see output as <class 'list'> and so on


# creating a class in python named sample

class Sample():
    pass

x=Sample()

print(type(x))

# now we will  create a class with attributes and methods

class Dog():
    def __init__(self,breed):
        self.breed=breed
        pass
    # this is very important as it work as construtor and does initialization

mydog=Dog(breed="german SHephard")
otherDog=Dog(breed="husky")
print(mydog.breed)
print(otherDog.breed)
print(type(mydog))



# creating a class that can have breed and naem as attribute

class Dog ():
    def __init__(self , breed , name):
        self.breed=breed
        self.name =name

dog1=Dog(breed ="GS", name="kalua")
dog2=Dog(breed="husky", name ="charku")

print(dog1.name , dog1.breed)
print(dog2.name , dog2.breed)




# creating a class that can have breed and naem as attribute as well as a globa variablae that 

class Dog ():

    species="MAMAL"
    def __init__(self , breed , name):
        self.breed=breed
        self.name =name

dog1=Dog(breed ="GS", name="kalua")
dog2=Dog(breed="husky", name ="charku")

print(dog1.name , dog1.breed)
print(dog2.name , dog2.breed)

print("Species of  dog is " , Dog.species)




# adding function along with the attribute so to mak eit work proper

class circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return circle.pi*self.radius**2 
        


a1=circle(3)
print(a1.radius)
print(a1.area())

 
#   changing the value of radius  outisde of class
class  Circle():
    pi=3.14
    def  __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        return Circle.pi*self.radius**2
    
    def change_Radius(self, newr):
        self.radius=newr


ci=Circle(radius=5)
print(ci.radius)
print(ci.area())

# changing the raius from direectly calling the attribute via object
ci.radius=1000
print(ci.radius)
print(ci.area())

# calling directlty thrugh the setter funcion in class CIRCLE
ci.change_Radius(newr=10)
print(ci.radius)
print(ci.area())

