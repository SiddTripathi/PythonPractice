#sets are non repetetive lists. See Example below

sample1 = "my name is sid sid is my name"

print(set(sample1.split()))

#we can also perform various functions on sets such as union, intersection etc. 

#For example, below is the sets of people who attended two events a and b

a = set(["Sidd","Neha","Jaya","Pratibha"])
b = set(["Prakhar","Chandan","Shobhit","Jaya","Sidd"])

#list of all the people in a and b

print(a.union(b))

#list of people who attended both events

print(a.intersection(b))

#list of people who attended any one of the event

print(a.symmetric_difference(b))

#list of people who attended only event b

print(a.difference(b))

#list of people who attended only event a

print(b.difference(a))


