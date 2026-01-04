class Animal:                                                 #parent and child
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()





class Animal:                              #granparent ,parent and child
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.walk()
d.bark()




class Animal:                                                      #parent to child 1 and chil2
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()





class Father:                                                                         #from parent 1 and parent 2 to child
    def work(self):
        print("Father works")

class Mother:
    def care(self):
        print("Mother cares")

class Child(Father, Mother):
    def study(self):
        print("Child studies")

c = Child()
c.work()
c.care()
c.study()
