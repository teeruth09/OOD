# จงเขียนโปรแกรมเพื่อรับข้อความ แล้วให้แสดงผล จำนวนตัวอักษรพิมพ์ใหญ่ และ พิมพ์เล็ก และแสดงตัวอักษรที่พบ เรียงตามลำดับตัวอักษร โดยไม่แสดงตัวอักษรซ้ำ 
# และให้แสดงผลตามตัวอย่าง

# หมายเหตุ ให้ระวังตัวอักษรตัวใหญ่ตัวเล็ก ให้ดี

#  *** String count ***
# Enter message : I Love KMITL.
# No. of Upper case characters : 7 
# Unique Upper case characters : I  K  L  M  T                 # ตัวแรกวรรคเดียว ที่เหลือ 2 วรรค
# No. of Lower case Characters : 3                                                    ##########C ใหญ่
# Unique Lower case characters : e  o  v  

#  *** String count ***
# Enter message : I see the questions in your eyes. I know what's weighing on your mind. You can be sure I know my part.
# No. of Upper case characters : 4
# Unique Upper case characters : I  Y  
# No. of Lower case Characters : 73
# Unique Lower case characters : a  b  c  d  e  g  h  i  k  m  n  o  p  q  r  s  t  u  w  y  

print(" *** String count ***")
message = input("Enter message : ")
up_num = 0
low_num = 0
up_character = ""
low_character = ""
up_list = []
low_list = []
for i in message:
    #print(message[i])
    if i.islower():
        low_num +=1
        low_character = i
        #print(low_num)
        if i not in low_list :
            low_list.append(i)
        # for check in low_list:
        #     if check != low_character:
        #         low_list.append(low_character)              #checlk ตัวอักษรซ้ำ
            

    if i.isupper():
        up_num +=1
        up_character = i
        #print(up_num)
        # up_list.append(up_character)
        if i not in up_list:
            up_list.append(i)
        # for check in up_list:
        #     if check != up_character:
        #         up_list.append(up_character) 
    up_character = ""
    low_character = ""
sort_up = sorted(up_list)
sort_low = sorted(low_list)
#print(f"Enter message : {message}")
print("No. of Upper case characters :"+" "+str(up_num))
print(f'Unique Upper case characters : {"  ".join(sort_up)}')
print("No. of Lower case Characters :"+" "+str(low_num))
print(f'Unique Lower case characters : {"  ".join(sort_low)}')
# print(sorted(up_list))
# for c in up_list:
#     print(c,end=" ")