class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        add_result=self.num1+self.num2
        return add_result

    def subtract(self):
        sub_result=self.num2 - self.num1
        return sub_result

    def multiply(self):
        mul_result=self.num1*self.num2
        return mul_result

    def divide(self):
        div_result=self.num2/self.num1
        return div_result

obj = Calculator(10, 94)
addtion=obj.add()
print("Addition: ",addtion)
substarction=obj.subtract()
print("Substraction: ",substarction)
multiplication=obj.multiply()
print("Multiplication: ",multiplication)
divison=obj.divide()
print("Division: ",divison)
