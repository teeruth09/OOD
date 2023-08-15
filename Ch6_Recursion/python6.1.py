'''

จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

โดยแสดงผลตามตัวอย่าง

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def print1ToN(n):
    #code here

def printNto1(n):
    #code here

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)


Enter Input : 6
1 2 3 4 5 6 6 5 4 3 2 1 

Enter Input : -1
1 1 

Enter Input : 0
1 1 

Enter Input : 1
1 1 



'''
def print1ToN(n):
    #code here
    if n >=1:
        if n-1 != 0:
            print1ToN(n-1)
        print(n,end = " ")
    else:    
        print('1',end = " ")
        
    
def printNto1(n):
    #code here
    if n >=1:
        print(n,end=" ")
        if n-1 !=0:
            printNto1(n-1)
    else:    
        print('1')

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)
