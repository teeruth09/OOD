'''
Chapter : 10 - item : 2 - First Greater Value
 ส่งมาแล้ว 0 ครั้ง
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

Enter Input : 3 2 7 6 8/5
6

Enter Input : 3 2 7 6 8/5 6 12
6
7
No First Greater Value

'''
inp = input("Enter Input : ").split('/')
left = [int(x) for x in inp[0].split()]
right = [int(y) for y in inp[1].split()]

for i in right:
    temp = []
    for j in left:
        if j > i:
            temp.append(j)
    if len(temp) > 0:
        temp.sort()
        print(temp[0])
    else:
        print("No First Greater Value")
