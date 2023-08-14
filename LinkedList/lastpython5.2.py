'''
พี่บ่าวสงสัยหลักการทำงานของการ forward และ backward ของ browser เลยไปทำการศึกษามาปรากฎว่ามันใช้หลักการของ linkedlist ซึ่งบังเอิญตรงกับเนื้อหาที่น้องๆ 2D กำลังศึกษาอยู่พอดี พี่เลยอยากให้น้องๆรู้ว่าจริงๆแล้ว linkedlist นั้นมีประโยชน์มากๆเลย โดยหลักการทำงานมันมีอยู่ว่าหากเราเข้า a.com แล้วไป b.com ต่อและอยากกลับมาหน้าเดิมก็กดปุ่ม backward ก็จะกลับมาที่ a.com และหากเข้า c.com แล้วย้อนกลับมา ก็จะกลับมาได้แค่ a.com ไม่ว่าเราจะย้อนสักกี่ครั้ง b ก็ไม่กลับมา

"ก็เหมือนกับแก้วที่แตกไปแล้ว ก็ต้องซื้อใหม่ ต่อให้เป็น Nasa ก็พาเธอกลับมาไม่ได้เธอไปนอกใจ ไม่ได้ไปนอกโลก"

Example

Enter Input : E google.com,E facebook.com,B,E youtube.com,B,F

History : google.com -> facebook.com -> google.com -> youtube.com-> google.com -> youtube.com

BackPath : youtube.com -> google.com

Description

E -> เข้า URL นั้นๆ จะตามด้วย URL เสมอ

B -> Backward ย้อนกลับมา 1 ครั้งเสมอ

F -> Forward ไปข้างหน้า 1 ครั้งเสมอ

History ให้แสดงว่าเคยเข้า URL ไหนไปบ้าง

BackPath ให้แสดง hierarchy ของ Path ที่เราสามารถย้อนกลับไปได้โดยให้แสดงจาก current มา first

ปล. โดยทุกการเข้า URL จะเริ่มที่หน้า welcome ของ browser เสมอ แต่ไม่ต้องนำไปใส่ใน history หรือ backpath ดูตัวอย่างได้ที่ TestCase 2


Enter Input : E bxdman.com,E google.com,E facebook.com,B,E ce-isag.com
History : bxdman.com -> google.com -> facebook.com -> google.com -> ce-isag.com
BackPath : ce-isag.com -> google.com -> bxdman.com

Enter Input : E google.com,E facebook.com,B,E youtube.com,B,F
History : google.com -> facebook.com -> google.com -> youtube.com -> google.com -> youtube.com
BackPath : youtube.com -> google.com

Enter Input : E php.net,E book.hacktricks.xyz,E portswigger.net,B,E google.com,E kali.org,B,F
History : php.net -> book.hacktricks.xyz -> portswigger.net -> book.hacktricks.xyz -> google.com -> kali.org -> google.com -> kali.org
BackPath : kali.org -> google.com -> book.hacktricks.xyz -> php.net


Hidden Testcase

Enter Input : E guthib.com,E github.com,B,E google.com,E reg.kmitl.ac.th,E fast.com,B,F,E google.com

'''
class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next
    
    def __str__(self):
        return str(self.data)

    
class LinkStack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.all = []

    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:
                s+=" -> "
        # if self.isEmpty():
        #     return f'Empty'
        return s

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def Size(self):
        count = 0 
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        return count

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
            self.all.append(Node(data)) #all input
        else:
            new_node = Node(data)
            new_node.next = self.head #node.next = self.head
            self.head = new_node
            self.all.append(Node(data))
        self.size +=1

    def pop(self):

        if self.isEmpty():
            return None
        else:
            pop_node = self.head
            self.head = self.head.next #move head to next node
            self.size -=1
            return pop_node.data
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data #top of stack is at head of list
        
class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:
                s+=" -> "
        # if self.isEmpty():
        #     return f'Empty'
        return s


    def Size(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        return count
    
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self, item):
        newest = Node(item) #node will be new tail node
        if self.tail == None:
            self.head = self.tail = newest
            return 
        self.tail.next = newest #ต้องเปลี่ยน tail ไม่งั้นชี้ผิด
        self.tail = newest #update reference to tail node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next
        self.size -= 1
        if self.head == None:
            self.tail = None
        return temp
    
stack = LinkStack()
queue = LinkQueue()
back = LinkStack()

inp_data = [i for i in input("Enter Input : ").split(",")]
for i in inp_data:
    inp = i[0]
    if inp == 'E':
        val = i.split()
        while not back.isEmpty():
            back.pop()
        stack.push(Node(val[1]))
        queue.enqueue(Node(val[1]))

    elif inp == 'B':
        if stack.Size() != 1:
            back.push(stack.pop())
            queue.enqueue(stack.peek())
        
        else:
            back.push(stack.pop())
    
    elif inp == 'F':
        if back.Size() >= 1:
            temp = back.pop()
            stack.push(temp)
            queue.enqueue(temp)
            
print(f'History : {queue.__str__()}')
print(f'BackPath : {stack.__str__()}')
