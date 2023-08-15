'''
จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

1. หาความยาวของ String

2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

3. Reverse String (ห้ามใช้คำสั่ง reversed)

4. ลบตัวอักษรที่ปรากฏมาก่อนใน String


Enter String and Number of Function : helloce 1
7

Enter String and Number of Function : aAaBbBccCDddd 2
AaAbBbCCcdDDD

Enter String and Number of Function : IloveKMITL 3
LTIMKevolI

Enter String and Number of Function : BananaBoat 4
Banot

'''

str1,str2 = input("Enter String and Number of Function : ").split()

change_size = []
revers_string = []
delete_string = []

class funString():

    def __init__(self,string):
        self.string = string

        ### Enter Your Code Here ###

    def __str__(self):
        ### Enter Your Code Here ###
        pass

    def size(self) :
        ### str 1
        return len(self.string)



    def changeSize(self):
        ### str 2
        for i in self.string:
            if ord(i) in range(65,90):
                j = int(ord(i))
                k = chr(j+32)
                change_size.append(k)
            elif ord(i) in range(97,122):
                j = int(ord(i))
                k = chr(j-32)
                change_size.append(k)
            else:
                continue
        return str("".join(change_size))


    def reverse(self):
        ### str3
        return str(self.string[::-1])
        
    def deleteSame(self):
        ### str 4
        for char in self.string:
            if char not in delete_string:
                delete_string.append(char)
        return str("".join(delete_string))
            


res = funString(str1)


if str2 == "1" :    
    print(res.size())

elif str2 == "2": 
    print(res.changeSize())

elif str2 == "3" : 
    print(res.reverse())

elif str2 == "4" : 
    print(res.deleteSame())
