'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())


* Stack Calculator *
Enter arguments : 5 6 +
11

* Stack Calculator *
Enter arguments : 3 DUP +
6

* Stack Calculator *
Enter arguments : 6 5 5 7 * - /
5

* Stack Calculator *
Enter arguments : a b c +
Invalid instruction: a

* Stack Calculator *
Enter arguments : 12
12

* Stack Calculator *
Enter arguments : 9 14 DUP + - 3 POP
19


* Stack Calculator *
Enter arguments : 1 2 3 4 5 POP POP POP
2

* Stack Calculator *
Enter arguments : 4 POP
0

'''

class calculator:
    def __init__(self):
        self.list = []
        self.operator = ['+', '-', '*', '/', 'DUP', 'PSH', 'POP']
        self.total = 0

    def push(self,value):
        return self.list.append(value)
    
    def pop(self):
        if not self.list:
            return 0
        return self.list.pop()
     
    def peek(self):
        if not self.list:
            return 0
        return self.list[-1]

    def run(self,arg):
        for i in arg:
            if i.isnumeric():
                self.push(i)
            elif i not in self.operator:
                self.total = f'Invalid instruction: {i}'
                return 
            else:
                if i == '+':
                    b = self.pop()          
                    a = self.pop()
                    if a.isalpha() == False and b.isalpha() == False:
                        result_sum = int(a) + int(b)
                        self.push(str(result_sum))
                elif i == '-':
                    d = self.pop() 
                    c = self.pop()
                    result_min = int(d) - int(c)
                    self.push(str(result_min))
                
                elif i == '*':
                    f = self.pop()
                    e = self.pop()
                    result_multi = int(f)*int(e)
                    self.push(str(result_multi))
                  
                elif i == '/':
                    j = self.pop()
                    i = self.pop()
                    result_div = int(j) / int(i)
                    self.push(str(int(result_div)))
                elif i == 'DUP':
                    top = self.peek()
                    dup = top
                    self.push(dup)
                elif i == 'POP':
                    top = self.pop()
                    
                elif i == 'PSH':
                    pass
        self.total = self.peek()
            
    def getValue(self):    
        return self.total


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = calculator()

machine.run(arg)
print(machine.getValue())

