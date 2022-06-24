#modules in python are just simple files with .py extension containing seperate peice of code.
#modules are imported using import command. Meaning, if you want to use functionality of one module in another then you need to import it.
#file name should be the class name. So that it is easier to import and use otherwise u need to access the class as I did in line 9
#notice that whenever import is executed, a .pyc file is created like __pychace__ folder. This file is cache which contains record of the imports, so that whenever file
# is run, it does not have to re-import. It just loads the modules from cache. Makes it faster.

# ******IMPORTANT***********
#if functions are inside a class, then as we know, we will need class import to access the function. So first import the class from another file, then access the 
# objects ( variables, methods etc) of that class. 
import sys




from sample import myFunct     
from sample import anotherFunc
from sample import myClass


class sampleClass:
    

    def myFunc(self):                              #always pass self parameter in a function inside class, or create a constructor (__init__) function to define variable
        print("this is present class")
        sample_class = myClass()                   # If you are accessing the functions inside of a class, then always first create instance of that class and then access the objects
        myFunct()
        anotherFunc()
        sample_class.func1()
        sample_class.func2()
       


testObj = sampleClass() #always remember, access methods inside a class by creating object of that class. 

testObj.myFunc()

#import all the things from file at once, use *

from Sample2 import *

testObj1 = calc()

print(testObj1.add(1,2))
print(testObj1.subtract(4,1))
msg()



#importing same module with different name called custom intitialization
# import myClass as class1
#import myClass as new_class

#singleton pattern python - basically singleton pattern means initiating once and using it again and again. bad me padhenge

#PYTHONPATH = /path python *filename* - this will tell interpreter to look for filename in specified path as well as local directory. Pythonpath is environment variable 
#so configure in windows environment variable
# sys.path.append - execute this before running the import command. 
sys.path.append("D:\Python_Pactice\PythonPractice")
import test_extending_Path

myExt = test_extending_Path.extendingPath()
myExt.testFunc1()



#built in modules - as we know there are lots of built-in python modules to do work. 

#to explore these modules, two very important functions are - dir and help

import re

find_members = []

for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))