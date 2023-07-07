'''
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

Enter Your List : -25 -10 -7 -3 2 4 8 10
[[-7, 2, 10], [-7, 4, 8]]

Enter Your List : -3 2 4 6 8 10
[[-3, 2, 6]]

Enter Your List : -100 100
Array Input Length Must More Than 2

Enter Your List : 5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
[[-5, 5, 5]]

'''
num =input("Enter Your List : ").split()
lst = []
for i in num:
    lst.append(int(i))

target_sum = 5
unique_combinations = set()

def find(input_nums):
    for i in range(len(input_nums)-2):
        for j in range(i+1, len(input_nums)-1):
            for k in range(j+1, len(input_nums)):
                if input_nums[i] + input_nums[j] + input_nums[k] == target_sum:
                    combination = sorted([input_nums[i], input_nums[j], input_nums[k]])
                    unique_combinations.add(tuple(combination))
    return unique_combinations
a = find(lst)
output = list(a)
#print(output)
result = []
for i in output:
    b =list(i)
    result.append(b)
if len(lst) < 3:
    print("Array Input Length Must More Than 2")
else:
    print(result)