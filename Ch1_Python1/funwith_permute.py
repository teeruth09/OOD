'''
เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด
*** Fun with permute ***
input : 1,2,3
Original Cofllection:  [1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

*** Fun with permute ***
input : 1,1,2,3
Original Cofllection:  [1, 1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]

'''
def change_position(list):
    present = list.copy()
    answer.append(present)
    collect = list.copy()
    for i in range(0,len(list)-1):
        old_num = collect[i]        #current           c=a
        collect[i] = collect[i+1]   #chaging to next position a=b       
        #a = new a
        collect[i+1] = old_num      #b=c
        current_list = collect.copy()
        answer.append(current_list)

def default(list):
    present = list.copy()         #current list
    change_position(list)         #do function one round
    for i in range(1, len(list)-1):
        for j in range(1, len(list)-1):
            old_num = present[j]
            present[j]= present[j+1]
            present[j+1]= old_num
            #get new present
            change_position(present)
        old_num = present[1]
        present[1] = present[len(list)-1]
        present[len(list)-1] = old_num
        if i != len(list)-2:
            change_position(present)

print("*** Fun with permute ***")
input_value = [int(k) for k in input("input : ").split(",")]
answer = []
print(f'Original Cofllection:  {input_value}')

first_index = input_value[::-1] #reverse list
default(first_index)
print(f'Collection of distinct numbers:\n {answer}')
