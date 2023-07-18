'''
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด


Enter people : Lorem_Ipsum
1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']

Enter people : JUST_DO_IT!!!!
1 ['U', 'S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J'] []
2 ['S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U'] []
3 ['T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U', 'S'] []
4 ['_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T'] []
5 ['D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_'] []
6 ['O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_', 'D'] []
7 ['_', 'I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] []
8 ['I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_']
9 ['T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_', 'I']
10 ['!', '!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I']
11 ['!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I', '!']
12 ['!', '!'] ['T', '_', 'D', 'O', 'T'] ['!', '!']
13 ['!'] ['_', 'D', 'O', 'T', '!'] ['!', '!']
14 [] ['_', 'D', 'O', 'T', '!'] ['!', '!']

Enter people : A_is_stand_for_amazing
1 ['_', 'i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A'] []
2 ['i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_'] []
3 ['s', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_', 'i'] []
4 ['_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's'] []
5 ['s', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_'] []
6 ['t', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_', 's'] []
7 ['a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] []
8 ['n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a']
9 ['d', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a', 'n']
10 ['_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n']
11 ['f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n', '_']
12 ['o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['_', 'f']
13 ['r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['_', 'f']
14 ['_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r']
15 ['a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r', '_']
16 ['m', 'a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_']
17 ['a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_', 'm']
18 ['z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['_', 'm', 'a']
19 ['i', 'n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['_', 'm', 'a']
20 ['n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i']
21 ['g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i', 'n']
22 [] ['d', 'o', 'a', 'z', 'g'] ['a', 'i', 'n']



'''

class queue:
    def __init__(self):
        self.main_row = []
        self.first_row = []
        self.second_row = []
    
    def main_pop(self):
        return self.main_row.pop(0)
    
    def row_pop(self,name):
        return name.pop(0)

    def push(self,row,value):
        return row.append(value)
    
    def size(self):
        return len(self.main_row)
    
people = input("Enter people : ")
que1 = queue()

for x in people:
    que1.push(que1.main_row,x)

for i in range(1,que1.size()+1):
    a = que1.main_pop()
    
    if len(que1.first_row) < 5:
        que1.push(que1.first_row,a)
        if len(que1.first_row) == 5:
            check = True
            status_minute = i                        #นาทีที่ครบ5
        else:
            check = False
    if i % 3 == 1 and i > 3:
        front_first_row = que1.row_pop(que1.first_row)
        if len(que1.first_row) < 5 and check == True:
            que1.push(que1.first_row,a)
            first_row_out_minute = i
        

    if check == True and i > status_minute + 1:
        if first_row_out_minute != i:
            #print(first_row_out_minute,i)
            que1.push(que1.second_row,a)
        if i % 2 == 0 and i > 9 :
            front_second_row = que1.row_pop(que1.second_row)
 
    print(f'{i} {que1.main_row} {que1.first_row} {que1.second_row}')