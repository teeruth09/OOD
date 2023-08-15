'''
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

Enter Input (L1,L2) : 1 2
L1    : 1 
L2    : 2 
Merge : 1 2 

Enter Input (L1,L2) : 1->2->3 4->5
L1    : 1 2 3 
L2    : 4 5 
Merge : 1 2 3 5 4

Enter Input (L1,L2) : I->Love->KMITL Datastruct->and
L1    : I Love KMITL 
L2    : Datastruct and 
Merge : I Love KMITL and Datastruct

Enter Input (L1,L2) : CE->2D Lardkrabang->KMITL
L1    : CE 2D 
L2    : Lardkrabang KMITL 
Merge : CE 2D KMITL Lardkrabang

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class  Linkedlist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        s = ""
        current = self.head
        while current != None:
            s += str(current.data)
            current = current.next
            if current != None:
                s += ' '
        return s

    def isEmpty(self):
        return self.head == None

    def append(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node #empty
        else:
            current = self.head
            while current.next != None:
                current = current.next #head = next
            current.next = new_node

    def reverse(self):
        
        prev = None
        current = self.head
        next = self.head.next
        while current is not None:
            next = current.next 
            current.next = prev
            prev = current
            current = next
            
        self.head = prev
        return self.head
    
lis1 = Linkedlist()
lis2 = Linkedlist()

inp = input("Enter Input (L1,L2) : ").split()

for i in inp[0].split("->"):
    lis1.append(i)
    
for j in inp[1].split("->"):
    lis2.append(j)
    

print(f'L1    : {lis1.__str__()}')
print(f'L2    : {lis2.__str__()}')
lis2.reverse()
print(f'Merge : {lis1.__str__()} {lis2.__str__()}')
