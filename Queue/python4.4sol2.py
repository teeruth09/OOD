'''
ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting



ตัวอย่างข้อมูลเข้า

Log : 0,3/0,7/2,3/7,7/10,5/10,1

คำอธิบาย

ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 

ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 

ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 

ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 

ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 

ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 



ไทม์ไลน์

เวลา(t)    เหตุการณ์

0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ

2    ลูกค้าคนที่ 3 เข้ามาในร้าน

3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที

6    ลูกค้าคนที่ 3 ได้กาแฟ

7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ

10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ

14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที

15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ



ผลลัพธ์ 

Time 3 customer 1 get coffee  

Time 6 customer 3 get coffee  

Time 7 customer 2 get coffee  

Time 14 customer 4 get coffee  

Time 15 customer 5 get coffee  

Time 15 customer 6 get coffee  

The customer who waited the longest is : 6

The customer waited for 4 minutes

 ***Cafe***
Log : 0,3/0,7/2,3/7,7/10,5/10,1
Time 3 customer 1 get coffee  
Time 6 customer 3 get coffee  
Time 7 customer 2 get coffee  
Time 14 customer 4 get coffee  
Time 15 customer 5 get coffee  
Time 15 customer 6 get coffee  
The customer who waited the longest is : 6
The customer waited for 4 minutes


 ***Cafe***
Log : 0,1/1,1/2,1/3,1/4,1/5,1
Time 1 customer 1 get coffee  
Time 2 customer 2 get coffee  
Time 3 customer 3 get coffee  
Time 4 customer 4 get coffee  
Time 5 customer 5 get coffee  
Time 6 customer 6 get coffee  
No waiting

 ***Cafe***
Log : 0,1/0,1/1,1/1,1/2,1/2,1
Time 1 customer 1 get coffee  
Time 1 customer 2 get coffee  
Time 2 customer 3 get coffee  
Time 2 customer 4 get coffee  
Time 3 customer 5 get coffee  
Time 3 customer 6 get coffee  
No waiting


'''

class Queue:
    def __init__(self):
        self.list_que = []

    def enqueue_list(self,value):
        self.list_que.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return 0
        else:
            return self.list_que.pop(0)
        
    def isEmpty(self):
        return len(self.list_que) == 0

    def size(self):
        return len(self.list_que)

    def top(self):
        return self.list_que[0]



class Customer: 
    def __init__(self, entry_time, time_per_cof, que):
        self.entry_time = entry_time
        self.time_per_cof = time_per_cof
        self.que = que

    def show_queue(self):
        return self.que
    def show_time_que(self):
        return self.entry_time
    def show_time_coffee(self):
        return self.time_per_cof
    



print(" ***Cafe***")
inp = input("Log : ").split("/")

queue = Queue()
time_line = 0

customer_deq = 0 
customer_deq2 = 0
que_front = 0
que = 1

barista1 = 1
barista2 = 1
time_make_bar1 = 0
time_make_bar2 = 0



save_wait = 0
save_index = 0
waiting = False



for x in inp:
    val = x.split(",")
    queue.enqueue_list(Customer(val[0],val[1],que))
    que += 1 

while not queue.isEmpty():
    if customer_deq:
        a = int(customer_deq.show_queue()) #custober number
    if customer_deq2:
        b = int(customer_deq2.show_queue())
    if customer_deq and customer_deq2:
        if int(customer_deq2.show_queue()) < int(customer_deq.show_queue()) and time_make_bar1 == time_make_bar2:
            tmp = int(customer_deq2.show_queue())
            b = a
            a = tmp
    if int(time_make_bar1) == time_line and time_make_bar1 != 0: #time linw = finish time
        print(f"Time {time_make_bar1} customer {a} get coffee")
        barista1 = 1 #barista ว่าง
        if int(queue.size()) != 0 and customer_deq != 0: #มีคิวต่อในแถว
            if int(time_make_bar1) - int(queue.top().show_time_que()) > int(save_wait):
                save_wait = int(time_make_bar1) - int(queue.top().show_time_que())
                save_index = int(queue.top().show_queue()) #เวลาแก้วก่อนหน้า
                waiting = True
    if int(time_make_bar2) == time_line and time_make_bar2 != 0: #time linw = finish time
        print(f"Time {time_make_bar2} customer {b} get coffee")
        barista2 = 1 #barista ว่าง
        if int(queue.size()) != 0 and customer_deq2 != 0: #มีคิวต่อในแถว
            if int(time_make_bar2) - int(queue.top().show_time_que()) > int(save_wait):
                save_wait = int(time_make_bar2) - int(queue.top().show_time_que())
                save_index = int(queue.top().show_queue()) #เวลาแก้วก่อนหน้า
                waiting = True
    if int(queue.size()) != 0:
        if barista1 and int(queue.top().show_time_que()) <= int(time_make_bar1) and int(queue.top().show_time_que()) <= int(time_line):
            time_make_bar1 = int(queue.top().show_time_coffee()) + time_make_bar1
            customer_deq = queue.dequeue()
            barista1 = 0 #ไม่ว่าง
    if int(queue.size()) != 0:
        if barista2 and int(queue.top().show_time_que()) <= int(time_make_bar2) and int(queue.top().show_time_que()) <= int(time_line):
            time_make_bar2 = int(queue.top().show_time_coffee()) + time_make_bar2
            customer_deq2 = queue.dequeue()
            barista2 = 0 #ไม่ว่าง
    if int(queue.size()) != 0:
        if barista1 and int(queue.top().show_time_que()) > int(time_make_bar1) and int(queue.top().show_time_que()) <= int(time_line):
            time_make_bar1 = int(queue.top().show_time_coffee())+ int(queue.top().show_time_que())
            customer_deq = queue.dequeue()
            barista1 = 0
    
    if int(queue.size()) != 0:
        if barista2 and int(queue.top().show_time_que()) > int(time_make_bar2) and int(queue.top().show_time_que()) <= int(time_line):
            time_make_bar2 = int(queue.top().show_time_coffee())+ int(queue.top().show_time_que())
            customer_deq2 = queue.dequeue()
            barista2 = 0
    time_line +=1

if customer_deq: 
    a = int(customer_deq.show_queue())
if customer_deq2:
    b = int(customer_deq2.show_queue())
if customer_deq and customer_deq2:
    if int(customer_deq2.show_queue()) < int(customer_deq.show_queue()) and time_make_bar2 == time_make_bar1:
        tmp = int(customer_deq2.show_queue())
        b = a 
        a = tmp
if time_make_bar1 == time_line:
    print(f'Time {time_make_bar1} customer {a} get coffee')
    barista1 = 1
if time_make_bar2 >= time_line:
    print(f'Time {time_make_bar2} customer {b} get coffee')
    barista2 = 1

if waiting:
    print(f"The customer who waited the longest is : {save_index}")
    print(f"The customer waited for {save_wait} minutes")
else:
    print(f"No waiting")      
