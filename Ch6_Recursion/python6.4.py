'''
Grouping 

แบ่งกลุ่ม  character โดยบอกว่า Character ตรง ตำแหน่งที่ Pin คือตัวอะไรและกลุ่มนั้นมีจำนวนเท่าไหร่

หากไม่มี String ให้แสดง Output : List is entry

หาก pin ที่ใส่มามากกว่าขนาดของ String ให้แสดง Output : Pin number out of range

หาก pin น้อยกว่า 1 ให้แสดง  Output : Pin number less than 1

******** ห้ามใช้ For / While ********

input : string,pin

Ex : 111112211002111,2

         string = 111112211002111

         pin = 2

               = 1(1)1112211002111 

         จำนวนในกลุ่ม = [11111],[22],[11],[00],[2],[111] = 5

******* Output *******

Character : 1

Count : 5

input number : 123456789,3
Character : 3
Count : 1

input number : abccasssdacccsd,4
Character : c
Count : 2

input number : ,1
Output : List is entry

input number : 12345,10
Output : Pin number out of range

input number : abc,0
Output : Pin number less than 1

input number : 1111111111111111111111111111111111111,10
Character : 1
Count : 37

input number : 111122333,5
Character : 2
Count : 2

input number : 11232558595959595559595,8
Character : 8
Count : 1

'''
inp = input("input number : ").split(',')
string = inp[0]
data_in_string = list(inp[0])
pin = int(inp[1])
index = 0
adress_pin = pin -1

def search(index):
    if len(data_in_string) > 0:
        if pin > 1:
            if index == adress_pin:
                print(f'Character : {data_in_string[index]}')
            elif index > len(data_in_string):
                print(f'Output : Pin number out of range')
            else:
                search(index+1)
        else:
            print(f'Output : Pin number less than 1')
    else:
        print(f'Output : List is entry')

search(0)
all_group = []
group = []

def seperate_group(index):
    if index < len(data_in_string) - 1:
        if data_in_string[index] == data_in_string[index+1] :
            group.append(data_in_string[index])
            seperate_group(index+1)
        else:
            group.append(data_in_string[index])
            all_group.append("".join(group))
            group.clear()
            seperate_group(index+1)
    else:
        group.append(data_in_string[index])
        all_group.append("".join(group))
        
if len(data_in_string) > 0:
    seperate_group(0)

count = 0

def find_group(pin,index,count):
    if pin-1 > count:
        if index < len(all_group):
            a = len(all_group[index])
            count += a
            if pin  > count:
                return find_group(pin,index+1,count)
            else:
                return a
    elif pin-1 <= count:
        return len(all_group[index])

count = find_group(pin,0,0)
if len(data_in_string) > pin and pin >0:
        print(f'Count : {count}')