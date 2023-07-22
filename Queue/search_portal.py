'''
พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
โดยรายละเอียดโปรแกรมจะมีดังนี้
Input
รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
ตัวอย่าง input: 3 3 F__,##_,O__
จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
F__
##_
O__
ภายในแผนที่
'F' แทนตำแหน่งเริ่มต้นของพี่
'O' แทนประตูทางออก
'_' แทนพื้นที่ที่สามารถเดินได้
ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
Output
หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
แสดง queue ระหว่างหาทางออก
ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."


Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(2, 1)]
Queue: [(2, 2)]
Queue: [(3, 2)]
Queue: [(3, 3)]
Queue: [(4, 3)]
Found the exit portal.

Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
Queue: [(3, 2)]
Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(2, 1), (4, 3), (2, 3)]
Queue: [(4, 3), (2, 3)]
Queue: [(2, 3), (5, 3)]
Queue: [(5, 3), (2, 4)]
Queue: [(2, 4), (5, 4)]
Queue: [(5, 4), (2, 5)]
Found the exit portal.

Enter width, height, and room: 3 3 ###,######F,###
Invalid map input.


Enter width, height, and room: 3 3 F__,##_,O_
Invalid map input.


Enter width, height, and room: 2 1 FO
Queue: [(0, 0)]
Found the exit portal.

Enter width, height, and room: 5 3 __|__,F_|_O,__|__
Queue: [(0, 1)]
Queue: [(0, 0), (1, 1), (0, 2)]
Queue: [(1, 1), (0, 2), (1, 0)]
Queue: [(0, 2), (1, 0), (1, 2)]
Queue: [(1, 0), (1, 2)]
Queue: [(1, 2)]
Cannot reach the exit portal.

Enter width, height, and room: 10 7 F_____\...,===\___\..,...#\___\.,....#|___|,...#/___/.,===/___/..,O_____/...
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(3, 0)]
Queue: [(4, 0)]
Queue: [(5, 0), (4, 1)]
Queue: [(4, 1), (5, 1)]
Queue: [(5, 1)]
Queue: [(6, 1), (5, 2)]
Queue: [(5, 2), (6, 2)]
Queue: [(6, 2)]
Queue: [(7, 2), (6, 3)]
Queue: [(6, 3), (7, 3)]
Queue: [(7, 3), (6, 4)]
Queue: [(6, 4), (8, 3), (7, 4)]
Queue: [(8, 3), (7, 4), (6, 5), (5, 4)]
Queue: [(7, 4), (6, 5), (5, 4)]
Queue: [(6, 5), (5, 4)]
Queue: [(5, 4), (5, 5)]
Queue: [(5, 5)]
Queue: [(5, 6), (4, 5)]
Queue: [(4, 5), (4, 6)]
Queue: [(4, 6)]
Queue: [(3, 6)]
Queue: [(2, 6)]
Queue: [(1, 6)]
Found the exit portal.

'''
class Queue:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.list_que = []
        self.position = []
        self.all_result = []
    def enqueue_list(self,value):
        self.list_que.append(value)
    def enqueue_position(self,value):
        self.position.append(value)
        self.all_result.append(value)
    def dequeue(self):
        return self.position.pop(0)
    def isEmpty(self):
        return len(self.position) == 0
    def size(self):
        return len(self.list_que)
    def size_position(self):
        return len(self.position)
    
que = Queue()

inp = input("Enter width, height, and room: ").split()

que.width = int(inp[0])
que.height = int(inp[1])

Map = inp[2].split(",")
check_F = ""

for i in Map:
    que.enqueue_list(i)
    check_F += i

Invalid_check = False

for y in range(que.height):
    if que.size() != que.height or len(que.list_que[y]) != que.width:
        print( "Invalid map input.")
        Invalid_check = True
        break


if Invalid_check == False :
    for y in range(que.height):
        for x in range(que.width):
            position = (x,y)
            if que.list_que[y][x] == 'F':
                que.enqueue_position(position)

if 'F' not in check_F:
    print( "Invalid map input.")


def show_position():
    while que.size_position() > 0:
        x, y = que.position[0]  # Get the first position from the queue
        que.dequeue()  # Dequeue the first position

        if y > 0 and que.list_que[y-1][x] == '_' and (x, y-1) not in que.all_result:  # north
            position = (x, y-1)
            que.enqueue_position(position)
        elif y > 0 and que.list_que[y-1][x] == 'O':
            print(f'Found the exit portal.')
            que.position = []
            break
        if x < que.width - 1 and que.list_que[y][x+1] == '_' and (x+1, y) not in que.all_result:  # east
            position = (x+1, y)
            que.enqueue_position(position)
        elif x < que.width - 1 and que.list_que[y][x+1] == 'O':
            print(f'Found the exit portal.')
            que.position = []
            break
        if y < que.height - 1 and que.list_que[y+1][x] == '_' and (x, y+1) not in que.all_result:  # south
            position = (x, y+1)
            que.enqueue_position(position)
        elif y < que.height - 1 and que.list_que[y+1][x] == 'O':
            print(f'Found the exit portal.')
            que.position = []
            break
        if x > 0 and que.list_que[y][x-1] == '_' and (x-1, y) not in que.all_result:  # west
            position = (x-1, y)
            que.enqueue_position(position)
        elif x > 0 and que.list_que[y][x-1] == 'O':
            print(f'Found the exit portal.')
            que.position = []
            break
        if que.position == []:
            print(f'Cannot reach the exit portal.')
        break
    
while que.size_position() > 0:
    print(f'Queue: {que.position}')
    show_position()