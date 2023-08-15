'''
รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น E คือ การ enqueue และ D คือการ dequeue 
แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input

ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน



input : D3,E2,E3,D9,E2,ff
Step : D3
Dequeue : []
Error Dequeue : 3
Error input : 0
--------------------
Step : E2
Enqueue : ['*0', '*1']
Error Dequeue : 3
Error input : 0
--------------------
Step : E3
Enqueue : ['*0', '*1', '*2', '*3', '*4']
Error Dequeue : 3
Error input : 0
--------------------
Step : D9
Dequeue : []
Error Dequeue : 7
Error input : 0
--------------------
Step : E2
Enqueue : ['*5', '*6']
Error Dequeue : 7
Error input : 0
--------------------
Step : ff
['*5', '*6']
Error Dequeue : 7
Error input : 1
--------------------

input : D3,D5,D9,D3,E12
Step : D3
Dequeue : []
Error Dequeue : 3
Error input : 0
--------------------
Step : D5
Dequeue : []
Error Dequeue : 8
Error input : 0
--------------------
Step : D9
Dequeue : []
Error Dequeue : 17
Error input : 0
--------------------
Step : D3
Dequeue : []
Error Dequeue : 20
Error input : 0
--------------------
Step : E12
Enqueue : ['*0', '*1', '*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*10', '*11']
Error Dequeue : 20
Error input : 0
--------------------


input : df,fs,E0,E2,D2,D3,ff,fd
Step : df
[]
Error Dequeue : 0
Error input : 1
--------------------
Step : fs
[]
Error Dequeue : 0
Error input : 2
--------------------
Step : E0
Enqueue : []
Error Dequeue : 0
Error input : 2
--------------------
Step : E2
Enqueue : ['*0', '*1']
Error Dequeue : 0
Error input : 2
--------------------
Step : D2
Dequeue : []
Error Dequeue : 0
Error input : 2
--------------------
Step : D3
Dequeue : []
Error Dequeue : 3
Error input : 2
--------------------
Step : ff
[]
Error Dequeue : 3
Error input : 3
--------------------
Step : fd
[]
Error Dequeue : 3
Error input : 4
--------------------

'''

class Queue:
    def __init__(self):
        self.list = []
        self.list_queue = []
        self.error_dequeue = 0
        self.error_input = 0
    def push(self,value):
        return self.list.append(value)
    def push_que(self, value):
        if self.list_queue:
            last_number = int(self.list_queue[-1][1:])
            if last_number >= 9:
                incremented_number = last_number + 1
                self.list_queue.append('*' + str(incremented_number))
            else:
                self.list_queue.append('*' + str(last_number + 1))
        else:
            self.list_queue.append(value)
    def peek(self):
        if self.list_queue:
            return self.list_queue[-1][1]                  #peek เลขล่าสุด
        else:
            return 0
    def pop(self):
        if not self.list:
            return 0
        else:
            return self.list_queue.pop(0)
    def size(self):
        return len(self.list)
    def que_size(self):
        return len(self.list_queue)
    
que = Queue()

inp = input("input : ").split(",")

found_d = False

for x in inp:
    que.push(x)
for i in range(que.size()):
    symbol = que.list[i][0]
    print(f'Step : {que.list[i]}')
    if symbol == 'D':
        number = int(que.list[i][1])
        before_update = int(que.peek())
        que.error_dequeue += number - que.que_size()
        que.list_queue = []
        print(f'Dequeue : {que.list_queue}')
        found_d =True
    elif symbol == 'E':
        if len(que.list[i]) == 2:
            number = int(que.list[i][1])
        elif len(que.list[i]) == 3:
            number = int(f'{que.list[i][1]}{que.list[i][2]}')

        for j in range(number):
            num_peek = int(que.peek())
            
            if found_d == True:
                num_peek = before_update
                found_d = False
            if num_peek == 0 and j == 0:
                que.push_que(f'*{num_peek}')
            else:
                que.push_que(f'*{num_peek+1}')
        print(f'Enqueue : {que.list_queue}')
        
    else:
        que.error_input +=1
        print(que.list_queue)

    print(f'Error Dequeue : {que.error_dequeue}')
    print(f'Error input : {que.error_input}')
    print("--------------------")