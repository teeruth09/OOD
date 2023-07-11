'''
ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้

def __init__()    // ใช้สำหรับสร้าง list ว่าง

def push(i)        // เก็บข้อมูลลง stack

def pop()          // นำข้อมูลออกจาก stack

def isEmpty()   // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false

def size()         // ตรวจสอบจำนวนข้อมูลใจ stack



แล้วให้โปรแกรมรับข้อมูล เพื่อเก็บใน stack และให้ทำงานตาม code คำสั่งต่อไปนี้

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)


 *** Stack implement by Python list***
Enter data to stack : K M I T L C E 2 5 6 3
11 Data in stack :  ['K', 'M', 'I', 'T', 'L', 'C', 'E', '2', '5', '6', '3']
0 Data in stack :  []


 *** Stack implement by Python list***
Enter data to stack : 1 2 3 4 5 6 7 8 9
9 Data in stack :  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
0 Data in stack :  []

 *** Stack implement by Python list***
Enter data to stack : 1.24 2.365 3653.2563 325336.2556 .3625 .35465 .85484
7 Data in stack :  ['1.24', '2.365', '3653.2563', '325336.2556', '.3625', '.35465', '.85484']
0 Data in stack :  []


 *** Stack implement by Python list***
Enter data to stack : we are computer engineer. I love KMITL.
7 Data in stack :  ['we', 'are', 'computer', 'engineer.', 'I', 'love', 'KMITL.']
0 Data in stack :  []


'''

class Stack:
    def __init__(self):
        self.items = []
        
        
    def push(self,string):
        self.items.append(string)

    def pop(self):
        if self.items :
            self.items.pop()


    def isEmpty(self):
        if not self.items :
            return True
        else:
            return False

    def size(self):
        
        return str(len(self.items))


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)
