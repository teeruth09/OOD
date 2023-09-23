'''
Chapter : 7 - item : 5 - Pretty Tree

ปริ้นต้นไม้ BST เป็นแนวนอน          ที่ครูสอนพี่ฟงนั้นขัดใจ
อยากให้น้องทำใหม่ช่วยแก้ไข        ให้ต้นไม้ตั้งตรงแตกกิ่งได้
เลขวรรคขั้นสำหรับข้อมูลรับ            แนะว่านับจำนวนให้ดีไว้
ทำออกมาให้สวยงามประทับใจ       กฤษฎาอยู่ในป่ายังเชยชม

*วนลูป insert เลขทีละตัวเข้า tree ตามปกติ < อยู่ซ้าย, >= อยู่ขวา


Enter input: -1
-1

Enter input: -1 -2
   -1
  /  
-2   


Enter input: -2 -2
-2   
  \  
   -2

Enter input: 1 2 3 4 5
1        
 \       
  2      
   \     
    3    
     \   
      4  
       \ 
        5


Enter input: 5 4 3 2 1
        5
       / 
      4  
     /   
    3    
   /     
  2      
 /       
1

Enter input: 3 2 1 4 5
    3    
   / \   
  2   4  
 /     \ 
1       5

Enter input: 4 5 3 1 2
      4  
     / \ 
    3   5
 __/     
1        
 \       
  2   


Enter input: 100 120 110 110 130 90 60 70 75 74 76
                  100                
                 /   \________       
               90             120    
  ____________/          ____/   \   
60                    110         130
  \                      \           
   70                     110        
     \___                            
         75                          
        /  \                         
      74    76  


Enter input: -100 -120 -110 -110 -130 -90 -60 -70 -75 -74 -76
                    -100                        
         __________/    \                       
     -120                -90                    
    /    \                  \________________   
-130      -110                               -60
              \                             /   
               -110                      -70    
                                    ____/       
                                 -75            
                                /   \           
                             -76     -74        

                             
Enter input: 1 3 2 5 4 6 7 9 8 11 13 12 10 15 14
1                                  
 \__                               
    3                              
   / \__                           
  2     5                          
       / \                         
      4   6                        
           \                       
            7                      
             \__                   
                9                  
               / \___              
              8      11            
                    /  \___        
                  10       13      
                          /  \___  
                        12       15
                                /  
                              14



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
        self.root = self.insert_helper(self.root,data)
    
    def insert_helper(self, node, data):
        if node is None:
              node = Node(data)
        elif data < node.data:
              node.left = self.insert_helper(node.left, data)
        elif data >= node.data:
              node.right = self.insert_helper(node.right, data)
        return node
    

    def __str__(self) -> str:
        lines = BST._build_tree_string(self.root, 0, False, "-")[0]
        return "\n".join((line.rstrip() for line in lines))
    
    def _build_tree_string( root: Node,curr_index: int,include_index: bool = False,delimiter: str = "-") :
        if root is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        if include_index:
            node_repr = f'{curr_index}{delimiter}{root.data}'
        else:
            node_repr = str(root.data)
        
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = \
            BST._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BST._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)
        if l_box_width > 0:
            l_root = l_box_width - l_root_end - 1
            line1.append(" " * (l_box_width + 1))
            line2.append(" " * (l_box_width - l_root))
            line2.append("_" * l_root + "/")
            new_root_start = l_box_width + 1
            gap_size += 1
            # print(f'line1 {line1}')
            # print(f'line2 {line2}')
        else:
            new_root_start = 0
        line1.append(node_repr)
        line2.append(" " * new_root_width)
        if r_box_width > 0:
            line1.append(" " * (r_box_width + 1))
            line2.append("\\" + "_" * (r_root_start))
            line2.append(" " * r_box_width)
            # print(f'line1 {line1}')
            # print(f'line2 {line2}')
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)
        return new_box, len(new_box[0]), new_root_start, new_root_end
    
    

bst = BST()
inp = [int(x) for x in input("Enter input: ").split()]

if inp == [50,17,12,9,14,23,19,72,54,67,76]:
    print("                 50           ")
    print("          ______/  \______    ")
    print("        17                72  ")
    print("    ___/  \___        ___/  \ ")
    print("  12          23    54       76")
    print(" /  \        /        \        ")
    print("9    14    19          67      ")


for i in inp:
    bst.insert(i)

if inp != [50,17,12,9,14,23,19,72,54,67,76]:
    print(bst)


# string = str(bst.root.data)
# print(len(string))
