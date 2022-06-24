#Unlike other languages, u dont need to mention data type in python. 


mynum = 1
name = "Siddharth"
Marks = 35.0
Heigt = float(6)

print(mynum)
print(name)
print(Marks)
print(Heigt)


total = Marks + Heigt #operator + can be used for concatenation. Only for same data type
#print(total) 41.0

#more than one assignment in one line
a,b = 3,4.0

print(a)
print(b)

#mixing operators between numbers/float and string is not allowed. hoever, number and float can be added result will be in float

#print(a+b) - 7.0

#print(a+name) - error


#exercise for above learning
mystring = "Hello"
myfloat = 10
myint = 20

if mystring == "Hello":
    print("String %s" %mystring)
if isinstance(myfloat, float) and myfloat == 10.0:  #myinstance returns true and false based on if the object matches the type lhs is object and rhs is type like string float etc.
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint ==20:
    print("Integ: %d" % myint)