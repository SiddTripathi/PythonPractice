#functions are defined using the 'def' keyword in python. Follows the block system. 

from audioop import add


def myfunction():
    print("my first function")


#function with argument

def userdetails(username, email):
    print("Hello User %s. Your Email is - %s. Welcome to tutorial" %(username, email))

userdetails("Siddharth", "siddhart.tripathi@gmail.com")

def evenodd(number):
    if(number%2==0):
        print("number is even")
    else:
        print("number is odd")

evenodd(5)

#return keyword. If you want to return a value at the end of function. Example

def addition(num1,num2):
    return num1+num2

print(addition(1,2))

#exercise In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
#Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
#Run and see all the functions work together!

def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

def build_sentence(info):
    return info+ " is a benefit of function"

def name_benefit_of_function():
    lists_benefits = list_benefits()
    for benefit in lists_benefits:
        print(build_sentence(benefit))

name_benefit_of_function()