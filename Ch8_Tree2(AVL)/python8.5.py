'''
Chapter : 8 - item : 5 - ตรวจสอบว่าเป็น binary search tree หรือไม่
 ส่งมาแล้ว 0 ครั้ง
จงเขียนฟังก์ชัน สำหรับตรวจสอบว่า Tree นี้เป็น binary search tree หรือไม่
โดยกำหนดให้ node.data มีค่าที่ต้องการอยู่ในช่วง 0<=node.data<=100 เท่านั้น และฟังก์ชั่นมี parameter มากที่สุด4ตัว


Enter Input : 2 1 3
      3
 2
      1
True


Enter Input : 1 2 3
      3
 1
      2
False


Enter Input : 1 0 5 101
      5
 1
      0
           101
False


Enter Input : 999 200 102 232
      102
 999
      200
           232
False


Enter Input : 1 0 2 0
      2
 1
      0
           0
False


Enter Input : 2 1 3 0 1
      3
 2
           1
      1
           0
False


Enter Input : 3 2 4 1 0 2 5
           5
      4
           2
 3
           0
      2
           1
False


Enter Input : 3 2 4 1 0 3 5
           5
      4
           3
 3
           0
      2
           1
False


Enter Input : 5 2 7 1 3 6 9
           9
      7
           6
 5
           3
      2
           1
True


Enter Input : 5 2 7 1 3 6 9 -8
           9
      7
           6
 5
           3
      2
           1
                -8
False




'''
class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root

            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)



def check_binary_search_tree_(root):
    #code here
    def is_bst_interenal(root, min_value, max_value):
        if root is None:
            return True
    
        if root.data < 0 or root.data > 100:
            return False
        
        if root.data <= min_value or root.data >= max_value:
            return False

        return (is_bst_interenal(root.left, min_value, root.data) and is_bst_interenal(root.right, root.data, max_value))
    return is_bst_interenal(root, min_value=float('-inf'), max_value=float('inf'))



tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)

print(check_binary_search_tree_(tree.root))