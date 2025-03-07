#Problem-1

"""
1.Define a class Person with instance object variables name and age, Provide  
___int__() method to set instance object variables. Also define methods to show name 
and age. Now define a subclass Employee of Person with instance object variable 
salary. Provide ___init__() method initialize instance object variable. Also define an 
instance method to show Employee data. 

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def showEmployee(self):
        print(self.name)
        print(self.age)
        print(self.salary)

emp = Employee("Ali", 25, 50000)
emp.showEmployee()


print("Problem no 2 ============")
#Problem-2
"""
2.Define a Class Account with instance object variables accountNo, balance and static 
variable rate_of_interst. Provide needful methods. Define subclass FixedDeposit of 
Account class with instance object variable time. Provide setter and getter. Also define a 
method to calculate simple interest.

"""

class Account:
    rate_of_interest=1
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance 
    @classmethod
    def setROT(cls,roi): #ROI= rate of interest
        cls.rate_of_interest=roi
class FixedDeosit(Account):
    def setTime(self,t):
        self.time=t
    def getTime(self):
        return self.time
    def simpleInterest(self):
        return self.balance*Account.rate_of_interest*self.time/100
    

fd=FixedDeosit(25,10000)
Account.setROT(5.5)
fd.setTime(2)
print("Rate of Interest =",fd.simpleInterest())


#problem-3
print("Problem no 3 ============")


"""
3.Demonstrate the use of super() in inheritance

"""

class A:
    def f1(self):
     print("A-f1")
class B(A):
    def f1(self):
        print("B-f1")
    def f2(self):

        self.f1()  
        super().f1()


obj=B()
obj.f2()


#problem-4
print("Problem no 4 ============")


"""
4.Define a class Account  with instance object variable balance with initial value as 0 
Provide withdrawal and deposit methods. Now define a subclass 
MinimumBalanceAccount of Account with provided minimum balance. Override 
withdrawal method according to minimum balance condition.

"""

class Account:
    def __init__(self):
        self.balance = 0
        
    def withdraw(self, amt):
        if self.balance > amt:
            self.balance = self.balance - amt

    def deposit(self, amt):
        self.balance = self.balance + amt

class MinimumBalanceAccount(Account):
    def setMinimumBalance(self, m):
        self.minimumBalance = m
        
    def withdraw(self, amt):
        if self.balance - self.minimumBalance > amt:
            self.balance = self.balance - amt

# Create Object
acc = MinimumBalanceAccount()
acc.deposit(1000)        # Deposit 1000
acc.setMinimumBalance(200)  # Set Minimum Balance
acc.withdraw(700)       # Withdraw 700

print("Remaining Balance:", acc.balance)



#problem-5
print("Problem no 5 ============")


"""
5.Define a class Polygon with instance object variable to store number of sides and a 
list of n side length values. Define a subclass Triangle of Polygon with instance methods 
getArea().

"""

class Polygon:
    def __init__(self,n,lengths): #lengts = lists
        self.n=n
        self.lengths=lengths

class Triangle(Polygon):
    def getArea(self):
        a,b,c=self.lengths # triangle 3 sides lenght is a,b,c values are stores in a,b,c  unpacked from list
        s=(a+b+c)/2 # semi paremeter formula 
        area=(s*(s-a)*(s-b)*(s-c))**0.5 # use hero formula with sqaure root 0.5 1/2
        return area 
    
t=Triangle(3,[3,4,5]) # 3 is no sides and as a list values of 3 sides 
print("Area is ", t.getArea()) 