


#problem_1

"""
1.Define a python class Person with instance object variables name and age. Set 
instance object variables in___int__() method. Also define show() method to display 
name and age of a person.


"""
class Person:
    def __init__(self, name, age):  # Fixed __init__ method
        self.name = name
        self.age = age  # Fixed age assignment
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
obj1 = Person("Suleman", 25)
obj1.show()



print("problem_2 ==================")
#problem_2
"""
2.Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods. 
"""

class Circle:
    def __init__(self):
        self.__radius = 0  # Private instance variable
    
    # Setter method for radius
    def setRadius(self, radius):
        self.__radius = radius
        
    # Getter method for radius
    def getRadius(self,):
        return self.__radius
    
    # Method to calculate Area
    def getArea(self):
        return 3.14 * self.__radius ** 2
    
    # Method to calculate Circumference
    def getCircumference(self):
        return 2 * 3.14 * self.__radius


# Object Creation
c = Circle()

# Setting Radius using Setter
c.setRadius(7)

# Getting Radius using Getter
print("Radius:", c.getRadius())

# Getting Area
print("Area:", c.getArea())

# Getting Circumference
print("Circumference:", c.getCircumference())


print("problem_3==================")
#problem_3

"""
3.Define a class Rectangle with length and breadth as instance object variables. 
Provide setDimensions(), showDimensions() and getArea() methods in it. 


"""
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def setDimensions(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def showDimensions(self):
        print("Length",self.length,"Breadth",self.breadth)

    def getArea(self):
        return self.length*self.breadth


# Object Creation
r = Rectangle(10, 5)

# Showing Initial Dimensions
r.showDimensions()
print("Area:", r.getArea())

# Updating Dimensions
r.setDimensions(15, 8)
print("\nAfter Updating Dimensions:")
r.showDimensions()
print("Area:", r.getArea())


print("problem_4==================")
#problem_4

"""
Define a class Book with instance object variables booked, title and price. Initialize 
them via ___int__() method. Also define a method to show book variables. 

"""


class Book:
    def __init__(self,id,title,price):
        self.bookid=id
        self.title=title
        self.price=price

    def show(self):
     print("Book ID:", self.bookid, "Title:", self.title, "Price:", self.price)

# Creating Object

b = Book(104, "Python Programming", 500.00)
# Showing Book Information
b.show()


print("problem_5==================")
#problem_5

"""

5.Define a class Team with instance object variable a list of team member names. 
Provide methods to input member names and display member names.


"""
class Team:

    def __init__(self):
        self.teamMemberNames=[]

    def inputMembers(self):
        print("Enter Member names separeted by comma")
        self.teamMemberNames=input().split(',')

    def displayMembers(self):
        for names in self.teamMemberNames:
            print(names)
t1 = Team()
t1.inputMembers()
t1.displayMembers()