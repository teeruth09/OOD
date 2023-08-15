'''
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" 
กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน 
เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย

class Stack:

    def __init__(self):

    def push(self, value):

    def pop(self):

    def size(self):

    def isEmpty(self):



inp = input('Enter Input : ').split()

S = Stack()

### Enter Your Code Here ###

print(S.size())

### Enter Your Code Here ###

Enter Input : G H H H H P
3
PHG

Enter Input : L C C X X X C D
2
DL
Combo : 2 ! ! !


Enter Input : C C C
0
Empty

Enter Input : A
1
A

Enter Input : A B B A
4
ABBA

Enter Input : O O P Y Y E R R R E E Y P P K K K O
0
Empty
Combo : 6 ! ! !

'''
class Stack:

    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def top(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop()
                
    def size(self):
        if self.list:
            return len(self.list)
        elif len(self.list) == 0:
            return str("0")

    def isEmpty(self):
        if not self.list:
            print("Empty",end = "")


inp = input('Enter Input : ').split()

S = Stack()
count = 0

for i in inp:
    S.push(i)
    if S.size() >= 3:
        top = S.pop()
        a = S.pop()
        b = S.pop()
        if top == a and top == b:
            count += 1
        else:
            S.push(b)
            S.push(a)
            S.push(top)


print(S.size())
if len(S.list) == 0:
    S.isEmpty()
print(''.join(S.list[::-1]))
if count >= 2 :
    print(f'Combo : {count} ! ! !')

