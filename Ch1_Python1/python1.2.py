# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 
# ให้ show ผลคูณของจำนวนทั้งสอง
# Testcase : #1 1
# *** multiplication or sum ***
# Enter num1 num2 : 20 30
# The result is 600
# Testcase : #2 2
# *** multiplication or sum ***
# Enter num1 num2 : 40 60
# The result is 100
print("*** multiplication or sum ***")

num1, num2 = input("Enter num1 num2 :"+" ").split()

n1 = int(num1)
n2 = int(num2)
if n1 * n2 > 1000:
    print("The result is "+str(n1+n2))
else:
    print("The result is "+str(n1*n2)) 