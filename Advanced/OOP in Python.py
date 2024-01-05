#CLASS
class Sample:
    print('This is new class')
x=Sample()#Calling a class
print(x)

#Attributes
'''self.attribute=Something
init()'''
class Dog:
    species='Mammal'
    def __init__(self,breed,food_quantity):
        self.breed = breed
        self.food_quantity=food_quantity

frak=Dog(breed='Huskie',food_quantity=2)
print(f"{frak.breed} breed of dog nees {frak.food_quantity} of packets per meal")

sam= Dog('Labrador',1)
print(sam.breed)
print(sam.food_quantity)
print(sam.species)

#CLASS METHODS
class Circle:
    pi=3.142
    #pi variable has become global for whole the class
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius * radius * Circle.pi
        #Can alse make equation of circumference as of area and also make another function
    #to use that pi value in the above function we will use it as cicle.pi and in any other function of that class we will use as self.pi
    def getcircumference(self,new_radius=5):
        return 2 * new_radius * self.pi
        #or return 2* self.radius*self.pi
c=Circle(3)
print(c.radius)
print(c.area)
print(c.getcircumference())


#INHERITANCE
class Animal:
    def __init__(self):
        print("Animal Created")
    def who(self):
        print("Animal")
    def eat(self):
        print("Eating")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")
    def who(self):
        print("Cat") 
    def cateat(self):
        print("Cat is eating") 

c=Cat()
print(c)  
a=Animal()
print(a)

c.who()
c.cateat()
c.eat()


#POLYMORPHISM

class dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"

class cat:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" says Meow!"
d=dog("Nik")
c=cat("Fussy")

print(d.speak(),'\n',c.speak())

p=[pet.speak() for pet in [d,c]]
print(p)

  