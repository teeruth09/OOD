'''
Chapter : 7 - item : 2 - หาค่า Min และ Max
 ส่งมาแล้ว 0 ครั้ง
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()


Enter Input : 10 4 20 1 5
      20
 10
           5
      4
           1
--------------------------------------------------
Min : 1
Max : 20



Enter Input : 4 10 3 6 13 9
           13
      10
                9
           6
 4
      3
--------------------------------------------------
Min : 3
Max : 13


Enter Input : 1 2 3 4 5 6 7 9 8 0 -1 -2
                                    9
                                         8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2
--------------------------------------------------
Min : -2
Max : 9

'''
class Node:
     def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None


class BST:
     def __init__(self):
          self.root = None
     
     def insert(self,data):
          self.root = self.insert_helper(self.root, data)
     
     def insert_helper(self, node, data):
          if node is None:
               node = Node(data)
          elif data < node.data:
               node.left = self.insert_helper(node.left, data)
          elif data > node.data:
               node.right = self.insert_helper(node.right, data)
          return node
    
     def print_tree(self):
          self._print_tree(self.root, 0)

     def _print_tree(self, node, indent):
          if node:
               self._print_tree(node.right, indent + 5)
               print(""," " * indent + str(node.data))
               self._print_tree(node.left, indent + 5)

     def search(self, value):
          return self._search_recursive(self.root, value)

     def _search_recursive(self, node, value):
          if node is None:
               return False
          if node.data == value:
               return True
          elif value < node.data:
               return self._search_recursive(node.left, value)
          else:# value > node.data
               return self._search_recursive(node.right, value)
          
     def search_last_leftmost(self):
          return self.search_left(self.root)
          
     def search_left(self,node):
          if node is None:
               return None
          else:
               while node.left is not None:
                    node = node.left
               return node.data

     def search_last_rightmost(self):
          return self.search_right(self.root)
          
     def search_right(self,node):
          if node is None:
               return None
          else:
               while node.right is not None:
                    node = node.right
               return node.data
  
bst = BST()
# inp = input("Enter INput : ").split()
inp = [int(x) for x in input("Enter Input : ").split()]
for i in inp:
    bst.insert(i)
                
bst.print_tree()
print("--------------------------------------------------")
     
print(f'Min : {bst.search_last_leftmost()}')
print(f'Max : {bst.search_last_rightmost()}')
