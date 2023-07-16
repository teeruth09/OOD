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
        self.total = 0

    def push(self,value):
        return self.list.append(value)
    
    def pop(self):
        return self.list.pop()
     
    def peek(self):
        return self.list[-1]

    def run(self,arg):
        for i in arg:
            if len(self.list) > 0:
                p = self.peek()
                if p == '+':
                    self.pop()
                    a = self.peek()
                    self.pop()
                    b = self.peek()
                    self.pop()
                    c = int(a)+int(b)
                    self.push(c)
                    
                elif p == '-':
                    self.pop()
                    a = self.peek()
                    self.pop()
                    b = self.peek()
                    self.pop()
                    c = int(a) - int(b)
                    self.push(c)
                elif p == '*':
                    self.pop()
                    a = self.peek()
                    self.pop()
                    b = self.peek()
                    self.pop()
                    c = int(a) * int(b)
                    self.push(c)
                elif p == '/':
                    self.pop()
                    a = self.peek()
                    self.pop()
                    b = self.peek()
                    self.pop()
                    c = int(a) / int(b)
                    self.push(c)
                elif p == 'DUP':
                    self.pop()
                    before_DUP = self.peek()
                    self.push(before_DUP)
                elif p == 'POP':
                    self.pop()
                    self.pop()
                elif p == 'PSH':
                    pass
            self.push(i)
            
    def getValue(self):
        for i in self.list:
            if not self.list:
                self.total = 0
            elif type(i) == str:
                if i.isalpha() == True:
                    print("Invalid instruction : "+self.list[0])
                else:
                    change = int(i)
                    self.total = change
            else:
                self.total = i
        
        return self.total


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = calculator()

machine.run(arg)
print(machine.getValue())
