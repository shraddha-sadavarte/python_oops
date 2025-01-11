from multiprocessing.reduction import send_handle
from tkinter.font import names
from math import pi

'''class human:
    pass
#simple class with method
class calci:
    def __init__(self,name): #constructor
        self.name=name #instant variable
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

c=calci("Basic calcii") #object creation with constructor
print("My calculator name is:",c.name)
print(id(c))
res=c.add(798,23)
print("Addition: ",res)
res=c.sub(798,23)
print("Subtraction: ",res)

#creating a mobile class with its functionalities
class mobile:
    def model(self,name):
        print("Model of mobile are: ",name)

    def color(self,cl):
        print("Color of mobile is: ",cl)

    def price(self,cost):
        print("Price of the mobile is: ",cost)

    def camera(self,front,back):
        print("Camera resolution is: ",front,"px",back,"px")

m1=mobile()
m1.model("Oppo")
m1.color("purple")
m1.price(13500)
m1.camera(50,120)
print(m1)'''

'''class Employee:
    company_name="Tech Corporation"
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display(self):
        print(f'The employee works in {self.company_name}')
        print(f'Employee id is {self.emp_id}')
        print(f'Employee name is {self.name}')
        print(f'Salary of employee {self.name} is {self.salary}')

e1=Employee(1231,"John",25000)
e1.display()'''

'''class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f'Brand of vehicle is {self.brand}')
        print(f'Model is {self.model}')

class Car(Vehicle):
    def __init__(self,brand,model, seating_capacity):
        super().__init__(brand,model) #call parent class constructor
        self.seating_capacity=seating_capacity
    def disp_car(self):
        print(f'Seating capacity {self.seating_capacity}')

# Creating Vehicle and Car objects
v1 = Vehicle("Toyota", "Corolla")
v1.display()  # Display details of the Vehicle

car1 = Car("Toyota", "Camry", 6)
car1.display()  # Display details from the Vehicle class
car1.disp_car()  # Display seating capacity from the Car class'''

'''class Computer:
    def __init__(self):
        self.__maxPrice=900 #private variable

    def sell(self):
        print(f'Selling price: {self.__maxPrice}')
    def setmaxprice(self,price):
        self.__maxPrice=price
#main program
c=Computer()
c.sell() #output selling price
c.__maxPrice=1000 #attempt to change the price directly
c.sell() #price does not change
c.setmaxprice(1000) #change the price using setter method
c.sell()'''

'''class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*self.radius**2

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

#function to calculate area of any shape
def calculate_area(shape):
    print('area: ',shape.area())

#creating instance of different shapes
c=Circle(5)
r=Rectangle(23,3)

#calculating areas
calculate_area(c)
calculate_area(r)'''

#method overloading (same method name with different parameters
class Calculator:
    def add(self, a, b):
        return a + b

    def add_three(self, a, b, c):
        return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

result1 = calc.add(5, 3) # Call method with two arguments (using the first method)
print(f"Sum of two numbers: {result1}")

result2 = calc.add_three(5, 3, 2) # Call method with three arguments (using the second method)
print(f"Sum of three numbers: {result2}")

#method overriding
class Animal:
    def speak(self):
        print("Animal is making a sound")

class Dog(Animal):
    def speak(self):  # Method overriding
        print("Dog is barking")

class Cat(Animal):
    def speak(self):  # Method overriding
        print("Cat is meowing")

# Create instances of subclasses
dog = Dog()
cat = Cat()

# Call the overridden methods
dog.speak()  # Output: Dog is barking
cat.speak()  # Output: Cat is meowing

