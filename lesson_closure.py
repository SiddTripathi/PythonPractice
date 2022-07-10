#A closure—unlike a plain function—allows the function to access 
# those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


def multiplier_of(n):
    def multiplier(number):
        
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))