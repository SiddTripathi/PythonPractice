#self will always be used in function

class calc:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        if(a<b):
            return b-a
        if(b<a):
            return a-b

def mult(a,b):
    return a*b

def msg():
    print("Function outside the class")

