'''
สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 

โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def isEmpty(self): return list นั้นว่างหรือไม่

4. def append(self, data): เพิ่ม data ต่อท้าย linked list

5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

class Node:
    def __init__(self, data):
        self.data = data


ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า

ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)

ตัวต่อไปจะอยู่ในรูปแบบ index:data

Enter Input : 1 2 3 4, 0:7, 3:9

ลิสต์ตั้งต้นคือ 1->2->3-> 4

ข้อมูล 0:0 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7

ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9



Enter Input : 1 2, 0:0, 3:3
link list : 1->2
index = 0 and data = 0
link list : 0->1->2
index = 3 and data = 3
link list : 0->1->2->3


Enter Input : 0 1 2, -1:3, 10:10
link list : 0->1->2
Data cannot be added
link list : 0->1->2
Data cannot be added
link list : 0->1->2


Enter Input : 0 1 2 4, 3:3
link list : 0->1->2->4
index = 3 and data = 3
link list : 0->1->2->3->4


Enter Input : ,0:0,1:1
List is empty
index = 0 and data = 0
link list : 0
index = 1 and data = 1
link list : 0->1


Enter Input : ,1:1
List is empty
Data cannot be added
List is empty

Enter Input : 0 1 2 4, -1:2, 3:3, 5:5, 0:-1
link list : 0->1->2->4
Data cannot be added
link list : 0->1->2->4
index = 3 and data = 3
link list : 0->1->2->3->4
index = 5 and data = 5
link list : 0->1->2->3->4->5
index = 0 and data = -1
link list : -1->0->1->2->3->4->5

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None
        self.size = 0
        
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:s+="->"
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t= self.head
            while t.next != None:
                t = t.next 
            t.next = p
        self.size +=1
            

    def insert(self, index, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        elif index == 0:
            p.next = self.head
            self.head = p 
        else:
            t = self.head
            i = 0
            while i<index-1:
                i+=1
                t = t.next
            p.next = t.next
            t.next = p
        self.size+=1

ls1 = LinkedList()

inp = [i.strip() for i in input("Enter Input :").split(',')]
l = inp[0].split()


for i in l:
    ls1.append(int(i))
if ls1.isEmpty():
    print("List is empty")
else:
    print("link list : "+ls1.__str__())
for i in inp[1:]:
    index,data = [int(j) for j in i.split(":")]
    if index<0 or index>ls1.size:
        print("Data cannot be added")
    else:
        ls1.insert(index,data)
        print("index = "+str(index)+" and data = "+str(data))
    if ls1.isEmpty():
        print("List is empty")
    else:
        print("link list : "+ls1.__str__())    
