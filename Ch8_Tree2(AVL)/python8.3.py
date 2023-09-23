'''
Chapter : 8 - item : 3 - Min-Max cost
 ส่งมาแล้ว 0 ครั้ง
จงหาค่า cost ที่น้อยที่สุดและมากที่สุดในการรวมเลขทั้งหมด

โดยค่า cost เกิดจากผลของการบวกเลข


อธิบาย test case 1

Input: 5 4 2 8

[5, 4, 2, 8] -> 4 + 2 -> 6

[5, 6, 8] -> 5 + 6 -> 11

[11, 8] -> 11 + 8 -> 19

Min cost = 6 + 11 + 19 = 36

 

[5, 4, 2, 8] -> 5 + 8 -> 13

[13, 4, 2] -> 13 + 4 -> 17

[17, 2] -> 17 + 2 -> 19

Max cost = 13 + 17 + 19 = 49



Enter Input: 5 4 2 8
Min cost: 36
Max cost: 49


Enter Input: 7 2 4
Min cost: 19
Max cost: 24


Enter Input: 100
Min cost: 0
Max cost: 0


Enter Input: 5 4 2 8 4
Min cost: 52
Max cost: 74


Enter Input: -5 -4 0 -8
Min cost: -47
Max cost: -30


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
class AVL_Tree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if node is None:
            return 0
        return node.height
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if node is None:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def rotate_right(self, y):
        x = y.left 
        T = x.right
        x.right = y
        y.left = T
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right 
        T = y.left
        y.left = x
        x.right = T
        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val <= root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data:
            root.right = self.insert(root.right, val)
        else:
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1 and val < root.left.data:
            return self.rotate_right(root)

        if balance < -1 and val > root.right.data:
            return self.rotate_left(root)

        if balance > 1 and val > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and val < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_val(self, val):
        self.root = self.insert(self.root, val)

    def get_cost(self):
        def ascending_traversal(node):
            if node is not None:
                ascending_traversal(node.left)
                ascending_list.append(node.data)
                ascending_traversal(node.right)

        ascending_list = []
        ascending_traversal(self.root)
        ascending_list = ascending_list.copy()
        descending_list = ascending_list[::-1].copy()
        min_cost = 0
        max_cost = 0

        while len(ascending_list) > 1:
            ascending_list.sort()
            descending_list.sort(reverse=True)
            # print(f'assce: {ascending_list} descen : {descending_list}')

            cost = ascending_list[0] + ascending_list[1]
            rev_cost = descending_list[0] + descending_list[1]
            min_cost += cost
            max_cost += rev_cost
            ascending_list = [cost] + ascending_list[2:]
            descending_list = [rev_cost] + descending_list[2:]

        return min_cost, max_cost

    def print_tree(self):
        def print_tree_helper(node, level=0):
            if node is not None:
                print_tree_helper(node.right, level + 1)
                print('     ' * level, node.data)
                print_tree_helper(node.left, level + 1)

        print_tree_helper(self.root)

tree = AVL_Tree()

inp = input("Enter Input: ").split()

for i in inp:
    tree.insert_val(int(i))

min_cost, max_cost = tree.get_cost()

print("Min cost: {}".format(min_cost))
print("Max cost: {}".format(max_cost))

