#lambda functions - are inline functions. You dont need to define them somewhere else and call them to use them. Instead,you can just define them at the place where you use them. 
#Lambda functions are useful for one time use

a,b = 4,6

sum = lambda a,b:a+b

print(sum(a,b))

#Check if number in given list is odd

l = [2,4,7,3,14,19]

chck_odd = lambda x : x%2==0

for i in l:
    print(chck_odd(i))



#multi argument - in a python function, more than one argument can be passed. You can either pre-declare arguments, or you can pass a variable number of argumet. The variable is a list of
#variables which recieves all arguments.The variable argument is declared by *

def foo(first,second,third,*options):
    print(first)
    print(second)
    print(third)
    print(options)


foo(1,2,3,4,5,6)

#keyword arguments are also allowed in order to avoid the order\sequence

def bar(first, second, third, **options):
    if options.get("action")=="sum":
        print("Sum is: %d" %(first+second+third))
    if options.get("number")=="first":
        return first

result = bar(1,2,3,action="sum",number="first")
print(result)