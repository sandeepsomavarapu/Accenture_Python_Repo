class Calculator:
    def __init__(self):
        print("am from default constructor")
    def sayHello(self):
        print("am from instance method")
    @classmethod
    def sayHi(cls,name):
        print("am from class method"+name)
    @staticmethod
    def addition(a,b):
        print("am from static  method, addition is:",a+b)
Calculator.sayHi("accenture")   #way to call classmethod     
calc=Calculator()
calc.sayHello()
Calculator.addition(10,20)