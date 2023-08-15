'''
ให้นักศึกษาแบ่งกลุ่มของสมาชิกใน linked list ที่ได้สร้างขึ้น โดยมีรายละเอียดในการเรียงใหม่เป็นดังนี้

1.) แบ่ง linked list ออกเป็นกลุ่มย่อยๆ g กลุ่ม กลุ่มละ k ตัว (หากเหลือเศษให้รวมเป็นอีกกลุ่มเลย)
2.) ในแต่ละกลุ่มให้วางสลับจาก หลัง มา หน้า (reverse) ทำทั้งหมด g กลุ่ม
3.) ถ้าใน linked list เป็นตัวเลขทุกตัว ระหว่างไป node ถัดไป ให้ใช้เครื่องหมาย "<->"
ถ้ามีตัวอักษร (string, character) ให้ใช้เครื่องหมาย ">" ในการเชื่อมระหว่าง node ทุก node
หมายเหตุ:

- หาก input ที่ได้รับมา ไม่มีอะไรเลย (เป็น string ว่าง) ให้แสดง "No elements in Linked List ? OK!"
- หาก Group's size ที่ได้รับมาน้อยกว่าหรือเท่ากับ 0 ให้แสดง "Group' size should be greater than 0"
แล้วออกจากโปรแกรม
โดยให้รับค่าตามตัวอย่าง

*** หากตรวจ Code ที่นักศึกษาส่งมา แล้วไม่พบว่ามีการแสดงผล Linked List และการเรียง
ลำดับใหม่ ตาม algorithm ที่ควรจะเป็น (ใช้ head ของ Linked List ในการวนหา Node ถัด
ไปมาแสดงผล หรือ ใช้ List ที่ได้ Input มาคำ นวนและแสดงผลเลย) จะส่ง Code กลับไปแก้ใหม่
และ ข้อนี้จะยังไม่ได้คะแนน จนกว่าจะใช้หลักการของ Linked List อย่างถูกต้อง ****

หมายเหตุ : มีข้อสงสัย ถามที่ TA ได้เลย

Enter the elements of Linked list/group's size: 1 2 3 4 5 6 7 8 9 0/5

Original Linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> 0
Modified Linked list: 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> 0 <-> 9 <-> 8 <-> 7 <-> 6


Enter the elements of Linked list/group's size: 1 2 3 4 5 6 7 8 9/3

Original Linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9
Modified Linked list: 3 <-> 2 <-> 1 <-> 6 <-> 5 <-> 4 <-> 9 <-> 8 <-> 7

Enter the elements of Linked list/group's size: 1 2 3 4 5/1

Original Linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
Modified Linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5

Enter the elements of Linked list/group's size: /0
No elements in Linked List ? OK!
Group' size should be greater than 0

Enter the elements of Linked list/group's size: a b c d e f g/5

Original Linked list: a > b > c > d > e > f > g
Modified Linked list: e > d > c > b > a > g > f


'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.number = 0
        self.size_node = 0
        self.group = 0


    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None and t.data.isnumeric():
                s+=" <-> "
            elif t != None:
                s+=" > "
        if self.isEmpty():
            return f'Empty'
        return s

    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def size(self):
        if self.head != None:
            self.size_node = 1
        current = self.head
        while current.next != None:
            current = current.next
            self.size_node += 1 
        return self.size_node
  
    
    def reverse_every_n_nodes(self, n):
        if n <= 1 or not self.head:
            return

        prev_group_end = None
        current = self.head

        while current: #current != None
            group_start = current #first = current
            group_prev = None
            
            i = 0

            while current and i < n:
                next_node = current.next
                current.next = group_prev
                group_prev = current
                current = next_node
                i += 1

            if prev_group_end:
                prev_group_end.next = group_prev
            else:
                self.head = group_prev

            prev_group_end = group_start

        if prev_group_end:
            prev_group_end.next = current


lis1 = Linkedlist()
inp = [e for e in input("Enter the elements of Linked list/group's size: ").split()]
seperate_group = inp[-1].split('/')
last_number = seperate_group[0]
for i in inp:
    if i == inp[-1]:
        lis1.append(last_number)
    else:
        lis1.append(i)

number = int(seperate_group[1])
if lis1.size() == 1:
    print("No elements in Linked List ? OK!")
    print("Group' size should be greater than 0")

elif number <=0:
    print("Group' size should be greater than 0")

else:
    print()
    
    print(f'Original Linked list: {lis1.__str__()}')

    lis1.reverse_every_n_nodes(number)
    print(f'Modified Linked list: {lis1.__str__()}')