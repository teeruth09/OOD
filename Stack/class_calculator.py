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
        return self.list.pop()
     
    def top(self):
        return self.list[-1]

    def run(self,arg):
        for i in arg:
            self.push(i)
            if i == '+':
                top = self.pop()       #pop sign  (+,-, *, /, DUP, POP, PSH)
                #print(top)
                b = self.pop()          #number before top(+)
                a = self.pop()
                if a.isalpha() == False and b.isalpha() == False:
                    result_sum = int(a) + int(b)
                    self.push(result_sum)
            elif i == '-':
                top = self.pop()
                #print(top)
                d = self.pop() #number before top(-)
                c = self.pop()
                result_min = int(d) - int(c)
                #print(result_min)
                self.push(result_min)
                #self.total -= result_min
            elif i == '*':
                top = self.pop()
                f = self.pop()
                e = self.pop()
                result_multi = int(f)*int(e)
                #print(result_multi)
                self.push(result_multi)
                #self.total *= result_multi
            elif i == '/':
                top = self.pop()
                j = self.pop()
                i = self.pop()
                result_div = int(j) / int(i)
                #print(result_div)
                self.push(int(result_div))
                self.total /=  int(result_div)
            elif i == 'DUP':
                top = self.pop()
                before_top = self.pop()
                dup = before_top
                self.push(before_top)
                self.push(dup)
            elif i == 'POP':
                if i == self.list[0]:
                    return 0
                top = self.pop()
                before_top = self.pop()
            elif i == 'PSH':
                #self.push(i)
                pass
            
    def getValue(self):
        for i in self.list:
            if not self.list:
                self.total = 0
            elif type(i) == str:
                if i.isalpha() == True :
                    
                    return str("Invalid instruction: "+i)
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

