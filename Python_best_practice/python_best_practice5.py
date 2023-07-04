'''
จงสร้าง class MyInt ซึ่งคลาสนี้เป็นคลาสที่เก็บเลขจำนวนเต็มโดยมี method ดังต่อไปนี้

__init__ สำหรับสร้างคลาส โดยรับจำนวนเต็มเพื่อใช้เป็นตัวแปรในคลาส

isPrime สำหรับตรวจสอบว่าตัวเลขนั้นเป็นจำนวนเฉพาะหรือไม่

showPrime สำหรับแสดงเลขจำนวนเฉพาะระหว่าง 2 ถึงเลขนั้น

__sub__ สำหรับลบค่าตัวตั้งด้วยค่าครึ่งหนึ่งของตัวลบ                                    20-(17//2)

โดยมีการเรียกใช้งานดังนี้

a = MyInt(20)

b = MyInt(17)

print(a.isPrime())                                        False

print(b.isPrime())                                        True

print(a.showPrime())                                     2 3  ....

print(b.showPrime())

print(a-b)

ผลลัพธ์

False

True

2 3 5 7 11 13 17 19 

2 3 5 7 11 13 17 

12

โดยให้เขียนโปรแกรมเพื่อรับค่า ตัวเลข 2 ตัว และแสดงผลดังตัวอย่าง

 *** class MyInt ***
Enter 2 number : 8 20
8 isPrime : False
20 isPrime : False
Prime number between 2 and 8 : 2 3 5 7 
Prime number between 2 and 20 : 2 3 5 7 11 13 17 19 
8 - 20 = -2

'''

class MyInt:
    def __init__(self, num):
        self._num = num
        
    
    def isPrime(self):
        #check prime number code

        if self._num < 2:
            return False
        for i in range(2,int(self._num ** 0.5)+1):
            if self._num % i == 0:
                return False
        return True

        # n = 2
        # while(int(self._num) % n != 0):
        #     n+=1
        # if self._num == str(n):
        #     return True
        # else:
        #     return False

            
        
    def showPrime(self):
        if(self._num < 2):
            return "!!!A prime number is a natural number greater than 1"
        prime_number = [] 
        for num in range(2, self._num+1):
            between_num = MyInt(num)
            if between_num.isPrime():
                prime_number.append(str(num))
        return " ".join(prime_number)

    def __sub__(self, num):
        return self._num - num._num // 2

print(" *** class MyInt ***")
#num1,num2 = input("Enter 2 number : "+" ").split()
num1, num2 = [int(x) for x in input("Enter 2 number : ").split()]

a = MyInt(num1)
b = MyInt(num2)

print(f'{a._num} isPrime : {a.isPrime()}')
print(f'{b._num} isPrime : {b.isPrime()}')
print(f'Prime number between 2 and {a._num} : {"".join(a.showPrime())}')
print(f'Prime number between 2 and {b._num} : {"".join(b.showPrime())}')
print(f'{a._num} - {b._num} = {a-b}')


