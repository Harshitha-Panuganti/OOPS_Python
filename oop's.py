class NewClass1:
    x=100
r=NewClass1()
print(r.x)

class Student:
    id=10
    name='Harshitha'
    def display(self):
        print(self.id,self.name)
s=Student()
s.display()

class Student:
    "This is a student class"
#     age=14
#     def welcome(self):
#         print("Hi, welcome to section B")
# print(Student.age)
print(Student.__doc__)

#Creating Object
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
x=Student('Harshitha',21)
print(x.name)
print(x.roll_no)

# #Modifing Object
x.name='Bhargavi'
print(x.name)

class Animal:
    def __init__(self,name):
        self.name=name 
    def greet(self):
        print("Hi, my name is",self.name)
a1=Animal('Dog')
a1.greet()

#Creating class and object
class Bike:
    def __init__(self,brandname,year):
        self.brandname=brandname
        self.year=year 
bmw=Bike('bmw',220)
print('{} year of manufacture'.format(bmw.year))

#Creating methods
class Bike:
    def __init__(self,brandname,year):
        self.brandname=brandname
        self.year=year
    def topspeed(self,topSpeed):
        self.topSpeed=topSpeed
        return "{} topspeed is".format(self.brandname,topSpeed)
    def type(self):
        return "{} is geared bike".format(self.brandname)
bmw=Bike("bmw",220)
print(bmw.topspeed(200))
print(bmw.type())

# Singlelevel inheritance Example
class Animal:
    def sound(self):
        print('Animal making sound')
class Cat(Animal):
    def Meow(self):
        print("Cat Meows")
d=Cat()
d.sound()
d.Meow()

# Multilevel inheritance
class Animal:
    def sound(self):
        print("Animal making sound")
class Cat(Animal):
    def Meow(self):
        print("Cat Meow")
class CatChild(Cat):
    def eat(self):
        print("Eating bread...")
d=CatChild()
d.sound()
d.Meow()
d.eat()

#Hierarchical inheritance
class employee:
   def __init__(self,name,age,salary):
      self.name=name 
      self.age=age 
      self.salary=salary
class Childemployee1(employee):
   def __init__(self,name,age,salary):
      self.name=name 
      self.age=age 
      self.salary=salary
class Childemployee2(employee):
   def __init__(self,name,age,salary):
      self.name=name 
      self.age=age 
      self.salary=salary
emp1=Childemployee1("Harshitha",21,28000)
emp2=Childemployee2("Bhargavi",19,25000)
print(emp1.name)
print(emp2.name)


# Polymorphism-(Polymorphism means having many forms same function name but used for differnt types)
class Parrot:
    def fly(self):
        print('Parrot can fly')
    def swim(self):
        print("Parrot can't swim")
class Penguin:
    def fly(self):
        print("Penguin can't swim")
    def swim(self):
        print("Penguin can swim")
blu=Parrot()
peggy=Penguin()
blu.fly()
peggy.fly()
blu.swim()

#Method overriding
class Bird:
    def intro(self):
        print("There are many types of birds.")
	
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

#Encapsulation - (Encapsulation is one of the cornerstone concepts of OOP. The basic idea of Encapsulation is to wrap up  both data and methods into one single unit.)
# There are 3 types of accessing variable 1)Public Members
                                        # 2)Private Members
                                     # 3)Protected Members
class Public_method:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("RollNo :" ,self.roll_no)
x=Public_method('Harshitha',28)
print(x.name)
x.display()

class Rectangle:
    def __init__(self):
        self.__length=5
        self.__breadth=6
        print(self.__length)
        print(self.__breadth)
x=Rectangle()
print(x.__length)

# Abstraction 
class Car():
   def milege(self):
      pass
class BMW(Car):
   def milege(self):
      print("The milege is 25kmph")
class Jaguar(Car):
   def milege(self):
      print("The mileage is 24kmph")
class Renault:
   def milege(self):
      print("The mileage is 27kmph")
t=BMW()
t.milege()
r=Renault()
r.milege()

