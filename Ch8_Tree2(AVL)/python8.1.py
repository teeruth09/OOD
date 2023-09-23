'''
Chapter : 8 - item : 1 - Huffman Encoding
 ส่งมาแล้ว 0 ครั้ง
ให้นักศึกษาเขียนโปรแกรมในการเข้ารหัส Huffman (บีบอัดข้อมูล) โดยใช้ Tree และแสดงผลตามตัวอย่าง

#อ่านวิธีการเข้ารหัสได้ที่ http://datastructurealgori.blogspot.com/2017/06/huffmans-code.html


Enter Input : ABACAB
{'A': '1', 'B': '01', 'C': '00'}
      A
 *
           B
      *
           C
Encoded! : 101100101


Enter Input : aaeeiiissttt
{'e': '111', 'a': '110', 't': '10', 'i': '01', 's': '00'}
                e
           *
                a
      *
           t
 *
           i
      *
           s
Encoded! : 1101101111110101010000101010


Enter Input : Hi!,happy happy code
{'o': '11111', 'i': '11110', 'e': '11101', 'd': '11100', 'c': '11011', 'H': '11010', ',': '11001', '!': '11000', 'p': '10', 'y': '011', 'h': '010', 'a': '001', ' ': '000'}
                          o
                     *
                          i
                *
                          e
                     *
                          d
           *
                          c
                     *
                          H
                *
                          ,
                     *
                          !
      *
           p
 *
                y
           *
                h
      *
                a
           *
                 
Encoded! : 110101111011000110010100011010011000010001101001100011011111111110011101


Enter Input : democraCy
{'a': '1111', 'C': '1110', 'y': '110', 'r': '101', 'o': '100', 'm': '011', 'e': '010', 'd': '001', 'c': '000'}
                     a
                *
                     C
           *
                y
      *
                r
           *
                o
 *
                m
           *
                e
      *
                d
           *
                c
Encoded! : 00101001110000010111111110110


Enter Input : CompressionDamn
{'s': '111', 'o': '110', 'n': '101', 'm': '100', 'p': '0111', 'i': '0110', 'e': '0101', 'a': '0100', 'D': '0011', 'C': '0010', 'r': '000'}
                s
           *
                o
      *
                n
           *
                m
 *
                     p
                *
                     i
           *
                     e
                *
                     a
      *
                     D
                *
                     C
           *
                r
Encoded! : 001011010001110000101111111011011010100110100100101


Enter Input : ThisIsHuffmanEncoding!
{'h': '11111', 'g': '11110', 'd': '11101', 'c': '11100', 'a': '11011', 'T': '11010', 'I': '11001', 'H': '11000', 'n': '101', 'E': '10011', '!': '10010', 'u': '1000', 's': '011', 'i': '010', 'f': '001', 'o': '0001', 'm': '0000'}
                          h
                     *
                          g
                *
                          d
                     *
                          c
           *
                          a
                     *
                          T
                *
                          I
                     *
                          H
      *
                n
           *
                          E
                     *
                          !
                *
                     u
 *
                s
           *
                i
      *
                f
           *
                     o
                *
                     m
Encoded! : 11010111110100111100101111000100000100100001101110110011101111000001111010101011111010010

'''

class Node:
     def __init__(self, data, freq, left = None, right = None) -> None:
          self.data = data
          self.freq = freq
          self.left = left
          self.right = right

     def __str__(self) -> str:
         return str(self.data)

class HuffmanTree:
     def __init__(self) -> None:
          self.root = None

     def insert(self, root: Node, data:str, freq:int) -> Node:
          if not root:
             return Node(data, freq)
          elif freq < root.freq:
              root.left = self.insert(root.left,data,freq)
          elif freq == root.freq:
               if data < root.data:
                    root.left = self.insert(root.left, data, freq)
               else:
                    root.right = self.insert(root.right, data, freq)
          else:
              root.right = self.insert(root.right, data, freq)
          return root

     def inorder(self, root: Node) -> list:
          if not root:
               return []
          return  self.inorder(root.right)+ [Node(root.data, root.freq)]+ self.inorder(root.left)


def print_tree(node: Node, level: int = 0) -> None:
     if node != None:
          print_tree(node.right, level + 1)
          print('     ' * level, node)
          print_tree(node.left, level + 1)

def get_code(root: Node, code: str) -> str:
     s = ''
     if root:
          s = get_code(root.right, code + '1')
          if root.data != '*':
               s += "'" + str(root.data) + "': '" + code + "'"
          a = get_code(root.left, code + '0')
          if a != '':
               s += ', ' + a
     return s

def search(root: Node, data: str, code: str) -> str: 
     if not root:
          return None
     if data == root.data:
          return code
     if root:
          s = search(root.right, data, code + '1')
          if s != None:
               return s
          s = search(root.left, data, code + '0')
          return s               


inp = [x for x in input('Enter Input : ')]
s = set(inp)
huffman = HuffmanTree()
for i in s:
     huffman.root = huffman.insert(huffman.root, i, inp.count(i))
data = huffman.inorder(huffman.root)
temp = [data.pop()]
while len(data) != 0 or len(temp) != 1:
     if len(temp) > 1:
          if data == [] or (data[-1].freq >= temp[0].freq + temp[1].freq):
               a, b = temp.pop(0), temp.pop(0)
               temp.append(Node('*',a.freq + b.freq, a, b))
          else:
               temp.append(data.pop())
     else:
          temp.append(data.pop())

print('{' + f'{get_code(temp[0], "")}' + '}') 
print_tree(temp[0])
print('Encoded! : ', end = '')
for i in inp:
     print(search(temp[0], i, ''), end = '')
