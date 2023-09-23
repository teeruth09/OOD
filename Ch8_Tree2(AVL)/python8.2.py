'''
Chapter : 8 - item : 2 - แฟ้มเอกสารสีฟ้า (Blue Archive)
 ส่งมาแล้ว 0 ครั้ง
    ในเมืองแห่งหนึ่งที่มีชื่อว่า คิโวโทส (Kivotos) ซึ่งสภาองค์กรนักเรียนของเราจะมีการเก็บรายชื่อนักเรียนในเมืองแบบ AVL Tree เรียกว่า "แฟ้มเอกสารสีฟ้า" โดยจะเก็บ data (ชื่อนักเรียน) และ key(ค่าของชื่อ โดยให้นำค่า ASCII ของตัวอักษรแต่ล่ะตัวในชื่อมาบวกกัน เช่น Arisu ก็จะเป็น 65+114+105+115+117=516 ก็จะเป็นค่า key ของนักเรียนคนนี้) ทางสภาองค์กรนักเรียน ต้องการเซนเซย์อย่างคุณ ช่วยเหลือสภาองค์กรนักเรียนทำ "แฟ้มเอกสารสีฟ้า" นี้ ให้สมบูรณ์ สู้ๆนะคะ เซนเซย์ จาก Arona

ข้อมูลนำเข้า

I data        นำชื่อนักเรียนเข้า "แฟ้มเอกสารสีฟ้า"

D data      นำชื่อนักเรียนออก "แฟ้มเอกสารสีฟ้า"

P               แสดงข้อมูลของ "แฟ้มเอกสารสีฟ้า"



ข้อมูลนำออกของ P

     การแสดงข้อมูลจะเป็นแบบ Tree Directory เผื่อไม่เห็นภาพ

'Root (Root.key)'

    'Left (Left.key)'

        'Left->Left (Left->Left.key)"

        *

    'Right (Right.key)'

        'Right->Left (Right->Left.key)

        'Right->Right (Right->Right.key)

ถ้าใน "แฟ้มเอกสารสีฟ้า" ไม่มี Left หรือ Right (ต้องมีอย่างใดอย่างนึง) ให้แสดง * แทนในส่วนที่ไม่มี (ตามตัวอย่าง) แต่ถ้าไม่มีทั้ง Left และ Right ก็ไม่ต้องแสดงอะไรเลย เพราะ เป็น leaf ของ AVL Tree

ทางองค์กรนักเรียนได้ทำการวาง Prototype ไว้แล้วตามนี้


testcase

Enter the data of your friend: I Arisu,I Neru,I Toki,I Momoi,I Midori,I Yuzu,P,D Toki,D Yuzu,P
------------------------------
Momoi (513)
    Neru (410)
        Toki (407)
        Yuzu (445)
    Arisu (516)
        *
        Midori (612)
------------------------------
Momoi (513)
    Neru (410)
    Arisu (516)
        *
        Midori (612)
------------------------------


Enter the data of your friend: I Arisu,I Neru,I Toki,I Momoi,I Midori,I Noa,I Hatsumi,I Mika,I Skul1CrowN,I Yuzu,P,D Arisu,D Noa,D Toki,D Yuzu,P,I Yaya,I Pom,I Sirati,I Bxdman,P
------------------------------
Neru (410)
    Mika (386)
        Noa (286)
        Toki (407)
    Arisu (516)
        Momoi (513)
            Yuzu (445)
            *
        Hatsumi (731)
            Midori (612)
            Skul1CrowN (953)
------------------------------
Midori (612)
    Neru (410)
        Mika (386)
        Momoi (513)
    Hatsumi (731)
        *
        Skul1CrowN (953)
------------------------------
Midori (612)
    Neru (410)
        Mika (386)
            Pom (300)
            Yaya (404)
        Momoi (513)
            *
            Bxdman (602)
    Hatsumi (731)
        Sirati (620)
        Skul1CrowN (953)
------------------------------


Enter the data of your friend: D Toki,P,I Saori,P,I Atsuko,I Hiyomi,I Koharu,I Hifumi,P,D Hiyomi,D Koharu,P
------------------------------
------------------------------
Saori (510)
------------------------------
Hiyomi (623)
    Hifumi (610)
        Saori (510)
        Koharu (618)
    Atsuko (631)
------------------------------
Hifumi (610)
    Saori (510)
    Atsuko (631)
------------------------------

Enter the data of your friend: I AAAAAA,I BBBB,I CCCCC,I DDDD,I EEEEEEEEEEE,P,D CCCCC,P
------------------------------
CCCCC (335)
    BBBB (264)
        *
        DDDD (272)
    AAAAAA (390)
        *
        EEEEEEEEEEE (759)
------------------------------
AAAAAA (390)
    BBBB (264)
        *
        DDDD (272)
    EEEEEEEEEEE (759)
------------------------------

'''
def nameValue(val):
    # Code Here
    key = 0
    for i in val:
        key += ord(i)
    return key


class TreeNode(object):
    def __init__(self, val):
        # Code Here
        self.key = val
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self) -> str:
        return str(self.key) + nameValue(self.key)


class AVL_Tree(object):
    
    
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if nameValue(key) < nameValue(root.key):
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if nameValue(key) < nameValue(root.left.key):
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if nameValue(key) > nameValue(root.right.key):
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
    def delete(self, root, key):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif nameValue(key) < nameValue(root.key):
            root.left = self.delete(root.left, key)
        elif nameValue(key) > nameValue(root.key):
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root



    def setHeight(self,root):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        root.height = 1 + max(a,b)
        return root.height

    def getHeight(self, root):#update height
        # Code here
        if not root:
            return 0
        return root.height 

    def getBalance(self, root):
        # Code here
        if not root:
            return 0 
        return self.getHeight(root.left) - self.getHeight(root.right)

    


    
        
    def leftRotate(self, z):
        # Code here
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y


    
    def rightRotate(self, z):
        # Code here
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
     
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def printTree(self, root, level=0):
        # Code here
        if root != None :
            indent = "    " * level
            print(indent + root.key,"(" + str(nameValue(root.key)) +  ")")
            self.printTree(root.left, level + 1)
            if (root.left is None and root.right is not None) or \
            (root.left is not None and root.right is None):
                print(indent + "    " + "*")
            self.printTree(root.right, level + 1)


avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    if data:
        data = data[0] 
    else:
        data = ""
    if op == "I":
        root = avl_tree.insert(root,data)

    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")
