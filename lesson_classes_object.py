#classes and objects are basically used for code reusability. You can create a function or variable once in class and use it multiple times by creating object of class
#Python passes an argument called “self” into every method in an object. “self” is similar to “this” in JavaScript. The “self” argument stores information about the values in an object.
#“self” is passed into methods by default because most methods rely on the values that have been assigned to an object in some way.
#add self to all methods in class to specify the object on which value is passed.
# or else you can create a __init__ function at begining where you can assign values to all the methods.


#self using __init__ method at top, you pass all the parameters while creating the object. You declare all the postional argument in __init__ method and the acces them using self
# like self.name in the any function u like. 

class MyClass:
    variable = "You are accessing class variable"

    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email

    def class_function(self):
        print("You are accessing class function %s" %self.name)
    
    def class_userDetails(self):
        print("Hello %s, your age is %d and email address is %s" %(self.name,self.age,self.email))


test_obj = MyClass("Sidd",23,"sidd@gmail.com")

print(test_obj.variable)
test_obj.class_function()
test_obj.class_userDetails()

#another method is without __init__ where you add self in every method along with the positional argument. You cannot access the name in userDetails method because now, name is local
#variable unlike the __init__

class MyClass:
    variable = "You are accessing class variable"

    def class_function(self, name):
        print("You are accessing class function %s" %name)
    
    def class_userDetails(self,age,email):
        print("Hello, your age is %d and email address is %s" %(age,email))


test_obj = MyClass()

print(test_obj.variable)
test_obj.class_function("sidd")
test_obj.class_userDetails(23,"sidd@gmail.com")


#exercise
class Vehicle:
    
    def __init__(self,name, color, kind, value):
        self.name=name
        self.kind=kind
        self.color=color
        self.value=value


    def description(self):
        desc_str = "%s is a %s %s worth $%.2f"%(self.name,self.color, self.kind, self.value)
        return desc_str
    

car1 = Vehicle("Fer","red","convertible",60000.00)
car2 = Vehicle("Jump","blue","van",10000.00)

print(car1.description())
print(car2.description())










