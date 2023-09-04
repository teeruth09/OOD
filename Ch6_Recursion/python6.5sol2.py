'''
พี่อยากให้น้องๆ หา string ทุกตัวที่เป็นไปได้จาก string ที่พี่ให้หน่อย ว่าง่ายๆ คือการประกอบคำนั่นเอง หรือที่เขาเรียกกันว่า String Permutation เป็นการเอาตัวอักษรแต่ละตัวจาก string ที่ให้ไปนำไปสร้าง string ที่มีความเป็นไปได้ทั้งหมด จากตัวอักษรของ string ที่ได้รับมา

Input มี 2 ค่า

string ที่จะนำมาหา Permutation
k = ขนาดของ string ที่จะสร้างขึ้นมาใหม่
โดยหลักการมีดังนี้

   1. ฟังก์ชัน `permute_string` รับพารามิเตอร์ 2 ตัวคือ string `s` และ integer `k` ที่แทนจำนวนตัวอักษรที่จะถูกสับเปลี่ยนตำแหน่ง
    2.ฟังก์ชันตรวจสอบว่า `k` มีค่าน้อยกว่า 0 หรือไม่ ถ้าใช่ จะเกิด `ValueError` ที่ระบุว่าไม่อนุญาตให้ใช้ค่า `k` ที่เป็นลบ โดยให้ return "Invalid value of k. k must be a non-negative integer."
   3. ภายในฟังก์ชัน `generate_permutations` มีการใช้ recursive เพื่อสร้างทุกความเป็นไปได้ของการสับเปลี่ยนตำแหน่งของความยาว `k` จาก string `s` ที่กำหนด. ถ้า `k` เป็น 0 จะ return เป็น string ว่าง
   4. ในส่วน recursion ฟังก์ชันวนลูปผ่านแต่ละตัวอักษรใน string `s` โดยนำตัวอักษรปัจจุบันมาเป็น "prefix" และสร้างการสับเปลี่ยนตำแหน่งของตัวอักษรที่เหลือโดยใช้ recursive ด้วยความยาวที่ลดลงเป็น `k - 1`
   6. ส่วนหลักการในการทำการสร้างการสับเปลี่ยนตำแหน่งทั้งหมดของความยาว `k` โดยใช้ฟังก์ชัน `generate_permutations` และในผลลัพธ์อาจมี string ที่สับเปลี่ยนแล้วซ้ำกัน ให้เปลี่ยนผลลัพธ์เป็น string ที่มีความ unique เท่านั้น เช่น ['abb', 'bab', 'bba', 'abb'] -> ['abb', 'bab', 'bba']
   7. สุดท้าย แต่ละ string ที่เป็นไปได้หลังจากหา unique และทำการ sorted

หมายเหตุ : ใครไม่รู้อะไร หรือ สงสัย สามารถสอบถาม TA ได้เลยครับ

Enter a string and k: abc/3
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Enter a string and k: TnT/2
['TT', 'Tn', 'nT']

Enter a string and k: aslkdjf;laskjdfienfnd/0
['']

Enter a string and k: aabbcc/1
['a', 'b', 'c']

Enter a string and k: xyz/90
Invalid value of k. k must be less than or equal to the length of the string.

Enter a string and k: unique/-123
Invalid value of k. k must be a non-negative integer.

'''

def permute_string(s, k):
    if int(k) > len(s):
        return 'Invalid value of k. k must be less than or equal to the length of the string.'
    elif int(k) < 0:
        return 'Invalid value of k. k must be a non-negative integer.'
    elif int(k) == 0:
        return '[\'\']'
    else:
        return 1
    
def count(s, c):
    temp = 0
    for i in s:
        if c == i:
            temp += 1
    return temp

def generate_permutation(s, k):
    global string, prev
    if k > 0:
        for i in string:
            if i not in prev:
                prev += i
                generate_permutation(prev, k-1)
            elif i in prev and count(prev, i) < char_count[i]:
                prev += i
                generate_permutation(prev, k-1)
        prev = prev[:-1]   
    else:
        result.append(prev)
        prev = prev[:-1]
        
temp_result = []
result = []
filtered_result = []
index = 0
len_string = 0
temp_k = 0
prev = ''
permuted_s = ''
string = ''
temp_string = string[:]
char_count = dict()
if __name__ == '__main__':
    string, k = input('Enter a string and k: ').split('/')
    temp_k = k
    len_string = len(string)
    for c in string:
        if c in char_count.keys():
            char_count[c] += 1
        else:
            char_count[c] = 1
    if permute_string(string, k) == 1:
        generate_permutation(string, int(k))
        for i in result:
            if i not in filtered_result:
                filtered_result.append(i)
        filtered_result.sort()
        print(filtered_result)
    else:
        print(permute_string(string, k))