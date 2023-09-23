'''
Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ
 ส่งมาแล้ว 0 ครั้ง
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

Enter Input : 6 3 -2 5 -8 2 -2
2 3 -2 5 -8 6 -2


Enter Input : 6 5 4 -1 3 0 2 -99 1
0 1 2 -1 3 4 5 -99 6

'''
def help_sort(l):
    for last in range(len(l)-1, 0, -1): #จาก last index to index 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1] :
                    l[i],l[i+1] = l[i+1], l[i] #swap
                    swaped = True
        if not swaped:
            break
    return l

def bubble_sort(l):
    for last in range(len(l)-1, 0, -1): #จาก last index to index 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1] and l[i] >= 0 and l[i+1] > 0 :
                    l[i],l[i+1] = l[i+1], l[i] #swap
                    swaped = True
        if not swaped:
            break
    return l

inp = input("Enter Input : ").split()
data = [int(x) for x in inp]
positive = [int(y)for y in inp if int(y) >=0]
bubble_sort(data)
help_sort(positive)
j = -1
for i in range(len(data)):
    if data[i] >=0:
        data[i] = positive[j+1]
        j = j+1
    else:
        continue
output = [str(x) for x in data]
print(' '.join(output))

