from tkinter.font import names


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

class Employee:
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
e1.display()