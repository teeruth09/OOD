'''
จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

#Test case 1
Enter num1 num2 : 5,5
10
0
25
1.0

#Test case 2
Enter num1 num2 : 20,5
25
15
100
4.0
'''
class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,x):
        self.x = x


    def __add__(self,num2):
        ###Enter Your Code For Add Number###
        return self.x+ num2.x

    def __sub__(self,num2):
        ###Enter Your Code For Sub Number### 
        return self.x - num2.x

    def __mul__(self,num2):
        ###Enter Your Code For Mul Number###
        return self.x * num2.x
    
    def __truediv__(self,num2):
        ###Enter Your Code For Div Number###
        return self.x / num2.x
x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")
