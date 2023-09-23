'''
Chapter : 9 - item : 4 - Find the Running Median
 ส่งมาแล้ว 0 ครั้ง
เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here


***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

- bubble sort

- straight selection sort

- insertion sort

- shell sort

- merge sort

- quick sort

- minHeap and maxHeap

พิมพ์คำตอบลงในช่อง Ans = "xxx"

***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***


Enter Input : 1 2 3 4 5 6 7 8 9
list = [1] : median = 1.0
list = [1, 2] : median = 1.5
list = [1, 2, 3] : median = 2.0
list = [1, 2, 3, 4] : median = 2.5
list = [1, 2, 3, 4, 5] : median = 3.0
list = [1, 2, 3, 4, 5, 6] : median = 3.5
list = [1, 2, 3, 4, 5, 6, 7] : median = 4.0
list = [1, 2, 3, 4, 5, 6, 7, 8] : median = 4.5
list = [1, 2, 3, 4, 5, 6, 7, 8, 9] : median = 5.0


Enter Input : 4 3 1 5 2 7 9 8
list = [4] : median = 4.0
list = [4, 3] : median = 3.5
list = [4, 3, 1] : median = 3.0
list = [4, 3, 1, 5] : median = 3.5
list = [4, 3, 1, 5, 2] : median = 3.0
list = [4, 3, 1, 5, 2, 7] : median = 3.5
list = [4, 3, 1, 5, 2, 7, 9] : median = 4.0
list = [4, 3, 1, 5, 2, 7, 9, 8] : median = 4.5


Enter Input : 5 4 3 2 1
list = [5] : median = 5.0
list = [5, 4] : median = 4.5
list = [5, 4, 3] : median = 4.0
list = [5, 4, 3, 2] : median = 3.5
list = [5, 4, 3, 2, 1] : median = 3.0


Enter Input : 12 4 5 3 8 7 83
list = [12] : median = 12.0
list = [12, 4] : median = 8.0
list = [12, 4, 5] : median = 5.0
list = [12, 4, 5, 3] : median = 4.5
list = [12, 4, 5, 3, 8] : median = 5.0
list = [12, 4, 5, 3, 8, 7] : median = 6.0
list = [12, 4, 5, 3, 8, 7, 83] : median = 7.0


'''
def bubble_sort(l):
    for last in range(len(l)-1, 0, -1): #จาก last index to index 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1], l[i] #swap
                swaped = True
        if not swaped:
            break
    return l


inp = input("Enter Input : ").split()
answer = []
data = []
median = 0
for i in inp:
    data.append(int(i))
    answer.append(int(i))
    bubble_sort(data)
    
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    

    print(f'list = {answer} : median = {float(median)}')

