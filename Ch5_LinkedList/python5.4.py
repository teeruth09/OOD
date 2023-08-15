'''
ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

โดยมีการรับ input ดังนี้

1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2

Enter input : A 0,A 1,S 2:0
0
0->1
Error! {index not in length}: 2
No Loop
0->1

Enter input : A 0,A 1,S 0:2
0
0->1
index not in length, append : 2
No Loop
0->1->2

Enter input : A 0,A 1,S 1:0
0
0->1
Set node.next complete!, index:value = 1:1 -> 0:0
Found Loop

Enter input : S 0:0
Error! {list is empty}
No Loop
Empty


Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
0
0->3
0->3->5
0->3->5->7
0->3->5->7->9
Set node.next complete!, index:value = 2:5 -> 0:0
Found Loop

Enter input : A 0,A 1,A 2,S 0:2
0
0->1
0->1->2
Set node.next complete!, index:value = 0:0 -> 2:2
No Loop
0->2


Enter input : S 0:0,A 0,A 0,A 0,S 0:5,S 0:3,A 5,S 2:1
Error! {list is empty}
0
0->0
0->0->0
index not in length, append : 5
Set node.next complete!, index:value = 0:0 -> 3:5
0->5->5
Set node.next complete!, index:value = 2:5 -> 1:5
Found Loop


Enter input : S 0:0,A 0
Error! {list is empty}
0
No Loop
0


Enter input : A 0,A -1,A -1,S 2:2
0
0->-1
0->-1->-1
Set node.next complete!, index:value = 2:-1 -> 2:-1
Found Loop

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.count_loop = 0

    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:
                s+="->"
        if self.isEmpty():
            return f'Empty'
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node #empty
        else:
            current = self.head
            while current.next != None:
                current = current.next #head = next
            current.next = new_node
        

    def search(self,index1,index2):
        if index1 == 0 and self.find_index(index1) == None:
            return f'Error! {{list is empty}}'

        if self.find_index(index1) == None:
            return f'Error! {{index not in length}}: {index1}'
        elif self.find_index(index2) == None:
            self.append(int(index2))
            return f'index not in length, append : {index2}'
        elif self.find_index(index1) != None and self.find_index(index2) != None:
            # return f'Set node.next complete!, index:value = {index1}:{self.find_index(index1)} -> {index2}:{self.find_index(index2)}'
            if index1 > index2:
                self.count_loop += 1
                i = 0
                cur_node = self.head
                pre = self.head
                while i < index1:
                    if i < index2:
                        pre = pre.next
                    cur_node = cur_node.next
                    #     cur_node = cur_node.next
                    # pre = pre.next
                    i += 1
                cur_node.next = pre
                return f'Set node.next complete!, index:value = {index1}:{cur_node.data} -> {index2}:{pre.data}'

            if index1 < index2:
                i = 0
                cur_node = self.head
                # print(f'cur_node {cur_node}')
                pre = self.head
                # print(f'pre {pre}')
                while i < index2:
                    if i < index1:
                        cur_node = cur_node.next
                    pre = pre.next
                    i += 1
                cur_node.next = pre
                return f'Set node.next complete!, index:value = {index1}:{cur_node.data} -> {index2}:{pre.data}'

            if index1 == index2:
                self.count_loop += 1
                i = 0
                cur_node = self.head
                pre = self.head
                while i < index1:
                    cur_node = cur_node.next
                    i+=1
                return f'Set node.next complete!, index:value = {index1}:{cur_node.data} -> {index2}:{cur_node.data}'

    def find_index(self,index):
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1
    
  

lis1 = Linkedlist()
inp_data = input("Enter input : ").split(",")

for i in inp_data:
    inp = i[0]
    if inp == 'A':
        val = i.split()
        for data in val[1:]:
            lis1.append(int(data))
        print(lis1.__str__())
    elif inp == 'S':
        val = i.split()
        index1,index2 = [int(j) for j in val[1].split(":")]
        print(lis1.search(index1,index2))
        
if lis1.count_loop > 0:
    print("Found Loop")
else:
    print("No Loop")
    print(lis1.__str__())
