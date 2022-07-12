#operators not only work for arthimatic operations but also help in concating the strings, creating lists of multiple repeating sequence

#arithmatic

number =  1+2-1*3/3
print(int(number))

#remainder of number, % 
remainder = 11%3
print(remainder)

#two multiplication symbol ** means to the power of

square = 2**2 #2 to the power 2 or 2 square
cube = 2**3 #2 to the power 3 or cube

print(square)
print(cube)

#Multiplying strings with number create lots of strings same 
manyhellos = "hello "*3
print(manyhellos)

#using operators with lists. 
list1 = [2,4,6,8]
list2 = [1,3,5,7]
total = list1 + list2 #this will concat the two lists or append the list2 in 1
print(total)

#repeating sequence list by multipying
list3 = [1,2,3]
rep_list = list3 *2
print(rep_list)

##########Exercise


x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")