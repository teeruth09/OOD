# เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล
# #Testcase : #1 1
# r=1.1
# Area=3.8013271108436504
# Testcase : #2 2
# r=0
# Area=0.0

r = float(input("r="))
Area = 3.141592653589793238*(r*r)
print("Area=" + str(Area))
