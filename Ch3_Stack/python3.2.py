'''
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง

Enter expresion : [[)))))
[[))))) Unmatch open-close  


Enter expresion : [[))
[[)) Unmatch open-close

Enter expresion : (())))
(()))) close paren excess

Enter expresion : )}]
)}] close paren excess


Enter expresion : (((
((( open paren excess   3 : (((

Enter expresion : (a+c)(a-b)*c(-a
(a+c)(a-b)*c(-a open paren excess   1 : (

Enter expresion : (([]))
(([])) MATCH

Enter expresion : (){}[]}
(){}[]} close paren excess
'''


class Stack:

    def __init__(self):
        self.list = []
        self.result = ""

    def push(self, value):
        self.list.append(value)

    def peek(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop()
                
    def isEmpty(self):
        if not self.list:
            s.result = "MATCH"

a = input("Enter expresion : ")
open = ['[','(','{']
close = [']',')','}']
s = Stack()
count = 0
check_close = 0
check_open = 0
for i in a:
    if len(s.list) > 0:
        top = s.peek()
        if top == '[' and i == ']':
            count +=1
            s.pop()
            continue
        elif top == '(' and i == ')':
            count +=1
            s.pop()
            continue
        elif top == '{' and i == '}':
            count +=1
            s.pop()
            continue

        for c in close:
            top = s.peek()
            if (top == '[' and (c == i and c != ']')) or (top == '(' and (c == i and c != ')')) or (top == '{' and (c == i and c != '}')):
                s.result= "Unmatch open-close"
                break    
    if i in open:
        s.push(i)
    elif i in close:
        s.push(i)
    

if s.isEmpty():
    print(f'{a} {s.result}')


for i in s.list:
    if i in close and s.result != "Unmatch open-close":
        s.result = "close paren excess"
    elif i in open and s.result != "Unmatch open-close":
        check_open +=1
        s.result = "open paren excess"

for i in s.list:
    if i in open and s.result != "Unmatch open-close":
        print(f'{a} {s.result}   {check_open} : {"".join(s.list)}')
        break
    else:
        print(f'{a} {s.result}')
        break
if len(s.list) == 0 :
    print(f'{a} {s.result}')
    
#print("".join(s.list))




