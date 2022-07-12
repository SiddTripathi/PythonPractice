#Map function has following syntax (func(), *iterables) - which means the function will be applied to each element of iterable
# THe MAP function in python 3 returns map object and hence we need to convert it to list using list() in order to iterate it

#Map helps us to implement a function on iterables easily.

#Exmpl - convert all strings in a list to upper case

import math


names = ["Harry","Tom","Dick","Alfred","Bruce"]

#if not map, then we would have used loops

upper_names = map(str.upper,names)
print(upper_names) #notice how the print statement gives a map object as result instead of list. Kyuki jaisa shuruat me likha hai ki Map function hmesha ek map object return krta hai 
print(list(upper_names))#ab agar isi object ko list me convert karke print karenge toh easily ho jaega

#Similarly, we can make exponential of number by its count, meaning square of 2 cube of 3 quadraple of 4 etc. Even if the range of iteration is beyond the actual iteration element, the map
#function will not throw any index out of bound error. It will simply return a list jaha tak bhi iteration ho sakta hoga. Bhale hi aap range me 1000 dedo. Jaha pe iteration khatam hoga
# wha tak ka result de diya jaega


num_list = [1,2,3,4,5]

result = list(map(math.pow,num_list,range(1,6)))

print(result)

#zip function is a function like map which creates a tuple of each of the iterables it takes as args. It does not matter if size of iterables is not same. It will zip the elements
#of the iterables untill one finishes. Just like map.

my_string = ['a','b','c','d','e']
my_numbers = [1,2,3,4,5,6]

rslt = list(zip(my_string,my_numbers))
print(rslt)