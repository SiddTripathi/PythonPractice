#Partial function is a higher order function. takes a function as input and constant values. It returns a function that can be used like other function


from functools import partial


def add(x,y):
    return x+y

smpl_partial = partial(add,5)

print(smpl_partial(5))

#the constant values start replacing variables from left to right. In above example, 5  replaces x where as smple_partial(5) replaces y. lets understand it with other example

def add_series(u,v,w,x,y,z):
    return u+v+w+x+y+z


add_prtial = partial(add_series,2,2,6,5) # The constant values here replace parameters of add_series from left to right. Also, out of 6 parameters original function, we passed
                                         # 4 constant values. That means the two variable parameters should be passed when partial function is called
print(add_prtial(6,4))

#So partial function is used if u want to derive a function (like add and add_series) with x parameters into a function with fewer parameter and fixed values to make it 
# a more limited functino

#****IMPORTANT NOTE***
#The constant values you pass in partial replace the parameters of actual function from left to right.