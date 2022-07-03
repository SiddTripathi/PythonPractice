#So basically, generator functions are functions which have yield instead of return. This means that after they are called, they yield a value and then pause at current state
# When they are called again then they resume from paused state. In normal functions we use return. Return terminates function while yield pauses it.
#More practice to be done.
#Since generator function generates sequece of objects, we need to have a for loop to access it.


import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)
    
    return
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))


def fib():
    a, b = 1, 1
    while 1:
        
        yield a
        a, b = b, a + b
        
        

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break