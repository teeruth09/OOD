'''
Chapter : 7 - item : 3 - Less Than or Equal
ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k



Enter Input : 10 4 20 1 5/4
      20
 10
           5
      4
           1
--------------------------------------------------
2


Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100/-101
                100
           75
                62
      50
                28
           25
                13
 0
                -13
           -25
                -38
      -50
                -62
           -75
                -100
--------------------------------------------------
0



'''
class Node:
     def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None


class BST:
     def __init__(self):
          self.root = None
          self.counter = 0
     
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
          
     # def search_last_leftmost(self):
     #      return self.search_left(self.root)
          
     # def search_left(self,node):
     #      if node is None:
     #           return None
     #      else:
     #           while node.left is not None:
     #                node = node.left
     #           return node.data

     # def search_last_rightmost(self):
     #      return self.search_right(self.root)
          
     # def search_right(self,node):
     #      if node is None:
     #           return None
     #      else:
     #           while node.right is not None:
     #                node = node.right
     #           return node.data

     def search_less(self,value):
          return self.search_less_help(self.root,value)
     def search_less_help(self, node, value):
          if node is not None:
               if node.data <= value:
                    self.counter += 1
               self.search_less_help(node.left, value)
               self.search_less_help(node.right, value)
               return self.counter
          
bst = BST()

list = input("Enter Input : ").split('/')

inp = [int(x) for x in list[0].split()]

k = int(list[1])

for i in inp:
    bst.insert(i)
                
bst.print_tree()
print("--------------------------------------------------")
print(bst.search_less(k))