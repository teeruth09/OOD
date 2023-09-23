'''
Chapter : 9 - item : 1 - หัดใช้ Sort
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง


Enter Input : -99 -1 0 1 2 3
Yes


Enter Input : 5252 -5 2630 -558
No


Enter Input : 9 10 99
Yes

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
data = [int(x) for x in inp]
default = [int(x) for x in inp]

if default == bubble_sort(data):
    print("Yes")
else:
    print("No")
