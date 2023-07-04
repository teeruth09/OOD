# จงคำนวณค่า BMI โดยมีสูตรการคำนวณดังนี้
# BMI = น้ำหนักหน่วย (kg) / ( ความสูงหน่วย (m) * ความสูงหน่วย (m))
# โดยมีเกณฑ์ดังต่อไปนี้
# ค่า                             สถานะ

# BMI < 18.5               Below normal weight

# 18.5 <= BMI < 25     Normal weight

# 25 <= BMI < 30        Overweight

# 30 <= BMI < 35        Case I Obesity

# 35 <= BMI < 40        Case II Obesity

# BMI >= 40                Case III Obesity

# โดยให้แสดงผลลัพธดังตัวอย่าง
#  *** BMI ***
# Enter your weight(kg) and height(m) : 48 1.68
# Your status is : Below normal weight.

#  *** BMI ***
# Enter your weight(kg) and height(m) : 58 1.71
# Your status is : Normal weight.
print(" *** BMI ***")
weight,height = input("Enter your weight(kg) and height(m) :"+" ").split()
w = int(weight)
h = float(height)
BMI = w/(h*h)
if BMI >= 40:
    print("Your status is : Case III Obesity.")
elif BMI >= 35:
    print("Your status is : Case II Obesity.")
elif BMI >= 30:
    print("Your status is : Case I Obesity.")
elif BMI >= 25:
    print("Your status is : Overweight.")
elif BMI >= 18.5:
    print("Your status is : Normal weight.")
else:
    print("Your status is : Below normal weight.")
    
