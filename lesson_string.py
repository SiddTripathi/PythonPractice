#uses c style string formating. %s for string %d for number integer and %f for float

name = "Nimesh"
print("my name is %s"% name)

my_list = [1,2,3]
print("this is a list %s" %my_list)

#exercise
data = ("John","Doe",53.44)
format_string = "hello"


#for float number, .(zero-precision)f is syntax. eg .2f means two decimal places.
print(format_string +" %s %s" %(data[0],data[1]) + " Your Current Balance is $%.2f" %data[2] )