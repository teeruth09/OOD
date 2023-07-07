'''
ให้เขียนโปรแกรมเพื่อหาลำดับของรหัสนักศึกษาที่กำหนด เมื่อเรียงลำดับตามคะแนน (ลำดับที่ 1 คือมีคะแนนมากที่สุด)

โดยรับข้อมูล รหัสนักศึกษา และ คะแนนเป็นเลขทศนิยม ที่ละบรรทัด

และจบด้วย รหัสนักศึกษา ที่ต้องการหาลำดับ

ในการคำนวณลำดับหากมีนักศึกษาที่ได้คะแนนเท่ากันให้เรียนลำดับตามรหัสนักศึกษา (เรียงแบบจำนวนเต็ม)

และให้แสดงผลดังตัวอย่าง

 *** Rank score ***
Enter ID and Score end with ID : 121 87.25 221 77.00 321 82.50 421 69.75 521 66.00 421
['121', '87.25', '221', '77.00', '321', '82.50', '421', '69.75', '521', '66.00']
421
{'121': 87.25, '221': 77.0, '321': 82.5, '421': 69.75, '521': 66.0}
4

 *** Rank score ***
Enter ID and Score end with ID : 111 100 13 96 1234 96 555 99 2121 96 99 99 1234
['111', '100', '13', '96', '1234', '96', '555', '99', '2121', '96', '99', '99']
1234
{'111': 100.0, '13': 96.0, '1234': 96.0, '555': 99.0, '2121': 96.0, '99': 99.0}
3

 *** Rank score ***
Enter ID and Score end with ID : 429801 78 359124 89 902316 91.25 773842 45.75 264336
['429801', '78', '359124', '89', '902316', '91.25', '773842', '45.75']
264336
{'429801': 78.0, '359124': 89.0, '902316': 91.25, '773842': 45.75}
Not Found

'''

result_dict = {}

id_and_score_collector = []


print(" *** Rank score ***")
id_and_score = input("Enter ID and Score end with ID : ").split()
for value in range(len(id_and_score)):
    id_and_score_collector.append(id_and_score[value])
    if value % 2 == 0:
        key = id_and_score_collector[value]
    elif value % 2 != 0:
        value = float(id_and_score_collector[value])
        result_dict[key] = value
    
ID = id_and_score_collector[-1]

id_and_score_collector.pop(-1)
print(id_and_score_collector)
print(ID)
print(result_dict)

# sorted_value = sorted(result_dict.values(), reverse=True)
# if ID in result_dict:
#     # rank = sorted_value.index(result_dict[ID])+1
#     # print(rank)
#     rank = sorted(sorted_value, reverse=True).index(result_dict[ID]) + 1
#     print(rank)
# else:
#     print("Not Found")
if ID in result_dict:
    sorted_score = sorted(set(result_dict.values()), reverse = True)
    rank = sorted_score.index(result_dict[ID])+1
    print(rank)
else: 
    print("Not Found")