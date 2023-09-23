'''
Chapter : 7 - item : 1 - King of Bi
 ส่งมาแล้ว 0 ครั้ง
สร้าง Binary Search Tree จากเลขที่ให้มา (วนลูป insert)
ให้หาว่ามีทั้งหมดกี่เส้นทาง แล้วในแต่ละเส้นทางผ่านกี่โหนด
print เรียงจากจำนวน path มากไปน้อย ถ้า path เท่าให้เรียงจาก node แทน
ปล. ทำไม่ได้โทษปอนด์

Test Case 1
Input
50 17 12 9 14 23 19 72 54 67 76

Binary Search Tree ที่ได้จาก input
                 50           
          ______/  \______    
        17                72  
    ___/  \___        ___/  \ 
  12          23    54       76
 /  \        /        \       
9    14    19          67


Output
5 path(s)
4 path(s) that pass through 3 node(s)
1 path(s) that pass through 2 node(s)


Enter input: 50 17 12 9 14 23 19 72 54 67 76
5 path(s)
4 path(s) that pass through 3 node(s)
1 path(s) that pass through 2 node(s)


Enter input: 4 2 1 3 7 5 8
4 path(s)
4 path(s) that pass through 2 node(s)


Enter input: 1 2 3 4 5
1 path(s)
1 path(s) that pass through 4 node(s)

Enter input: 5 4 3 2 1
1 path(s)
1 path(s) that pass through 4 node(s)


Enter input: 4 5 3 1 2
2 path(s)
1 path(s) that pass through 3 node(s)
1 path(s) that pass through 1 node(s)

Enter input: 100 120 110 130 90 60 70 75 74 76
4 path(s)
2 path(s) that pass through 5 node(s)
2 path(s) that pass through 2 node(s)


Enter input: 1 3 2 5 4 6 7 9 8 11 13 12 10 15 14
6 path(s)
1 path(s) that pass through 9 node(s)
1 path(s) that pass through 8 node(s)
1 path(s) that pass through 7 node(s)
1 path(s) that pass through 6 node(s)
1 path(s) that pass through 3 node(s)
1 path(s) that pass through 2 node(s)

'''
class Node:
    def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.path = 0
    
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

    def printPathtree(self):
        answer_list = []
        self.printPathtree_helper(self.root,[],answer_list)
        return answer_list
    

    def printPathtree_helper(self,root,res,answer_list):
        if root is None:
            return 
        res.append(root.data)
        # print(res)
        if root.left is None and root.right is None:
              answer_list.append(res.copy())
        self.printPathtree_helper(root.left,res,answer_list)
        self.printPathtree_helper(root.right,res,answer_list)
        res.pop()
        

    
    # def find_path(self,value=0):
    #     return self.find_path_help(self.root,value)

    # def find_path_help(self,node,value):
    #     if node is not None:
    #         if node.left is not None:
    #             value += 1 
    #         self.find_path_help(node.left,value)
    #         return value




bst = BST()

# inp = input("Enter INput : ").split()

inp = [int(x) for x in input("Enter input: ").split()]
for i in inp:
    bst.insert(i)

# print(bst.find_path())
answer = bst.printPathtree()

answer.sort(key=lambda x: len(x), reverse=True)

# print(answer)
print(f'{len(answer)} path(s)')

ans_dict = {}

for i in answer:
    if len(i) not in ans_dict:
        ans_dict[len(i)] = 0 #define
    ans_dict[len(i)] += 1

for k, v in ans_dict.items():
    print(f'{v} path(s) that pass through {k-1} node(s)')