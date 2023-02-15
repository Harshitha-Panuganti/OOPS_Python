# Single inheritance:
# In this type of inheritance, there is a single derived class from a single base class
class HomoSapiens:
    def speak(self):
        print("Homo sapiens speaking")
class Man(HomoSapiens):
    def talk(self):
        print("Man walking")
d=Man()
d.talk()
d.speak()


# Multi-level inheritance:
# In Multi-level inheritance, the derived class is inherited from another derived class
class HomoSapiens:
    def speak(self):
        print("Homo sapiens speaking")
class Man(HomoSapiens):
    def walk(self):
        print("Man walking")
class ManChild(Man):
    def eat(self):
        print("Eating food")
d=ManChild()
d.walk()
d.eat()

# Multiple inheritance:
# In Multiple inheritance, the derived class inherited from more than one base class
class Claculation1:
    def sum(self,x,y):
        return x+y; 
class Calculation2:
    def sub(self,x,y):
        return x-y;
class Derived(Claculation1,Calculation2):
    def multiple(self,x,y):
        return x*y; 
d=Derived()
print(d.sum(20,30))
print(d.sub(30,40))
print(d.multiple(20,50))


# Hierarchical inheritance:
# If more than one class is inherited from base class then it is known as hierarchical inheritance
class Blackandwhitetv:
    def antena(self):
        print("Channels are telecasted through anteena")
class ColorTv(Blackandwhitetv):
    def cableconnection(self):
        print("Channels are telecasted in tv through cable connection")
class WifiLEDTV(ColorTv):
    def AndroidApplication(self):
        print("You can watch movies on OTT platforms.")
a1=ColorTv()
a2=WifiLEDTV()
a1.antena()
a2.AndroidApplication()
a2.cableconnection()

# __init__ (function) is a constructor used to instance the object
# Example
class Person:
    def __init__(self,fname,lname):
        self.fname=fname 
        self.lname=lname 
    def display(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
x=Student('Harshitha','Panuganti')
x.display()

# Super keyword
class Person:
    def __init__(self,fname,lname):
        self.fname=fname 
        self.lname=lname 
    def display(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=Student('Harshitha','Panuganti')
x.display()

# issubclass keyword
class Claculation1:
    def sum(self,x,y):
        return x+y; 
class Calculation2:
    def sub(self,x,y):
        return x-y;
class Derived(Claculation1,Calculation2):
    def multiple(self,x,y):
        return x*y; 
d=Derived()
print(issubclass(Derived,Calculation2))
print(issubclass(Claculation1,Calculation2))

