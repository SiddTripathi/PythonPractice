#functions in pythons are objects. They can be assigned to variable and used
#A decorator is a kind of wrapper function arount original function to extend the funcitonality of the original function

from audioop import mul


def product(a,b):
    return a*b

print(product(2,3))

multiply =  product

#print(multiply(2,3))

#we can even pass functions as arguments

def sum(a,b):
    return a+b

def sub(a,b):
    if(a<b):
        return b-a
    else:
        return a-b

x,y=4,5
def result(func):
    
    rslt = func(x,y)
    print(rslt)

#result(sum)
#result(sub)


#We can return function from a function. Thats what we mean by closure. Retains the value. For instance agar yaha pe dekho - prod ke andar prod_child hai. prod function is closure and 
#and prod_child nested function hai. ab jaisa hm jante hain ki python me function ko as a variable store kar skte hai, toh agar koi function (like prod) function hi return kar rha hai, 
# to us variable se function call kr skte hai. mult variable me prod(5) jo bhi return karega woh store hoga. prod ne prod_child return kara jaha usne n ki value 5 se replace kar di
# toh basically, mult me prod ka return function hai. Ab hm mult ka use karke prod_child ko call kar skte hai with num as argument ( jo yaha 5 hai)

def prod(n):
    def prod_child(num):
        return num*n
    return prod_child

mult = prod(5)

print(mult(10))


#*******DECORATORS**************

def hello(func):
    print("test function")
    func()


@hello
def test():
    print("This is test function")

