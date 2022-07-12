#lists in python are arrays. 
#Can contain any type of variable and as many as you want
#indxing in lists start from zero.
#append() to add elements in list, insert if you want to insert at particular index.

numbers = []
strings = []

names = ["John","Eric","Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(type(names))

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The third name in array is %s" %names[2])
