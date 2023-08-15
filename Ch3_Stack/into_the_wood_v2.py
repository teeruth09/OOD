'''
<<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>

****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อบางคน Random ไม่ได้ครับ


หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง


Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
2
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
2
1
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
2
1
1
2


Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
0
0
1

Enter Input : A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
4
2
4
2

Enter Input : A 5,A 4,B,S,S,A 4,B
2
3

Enter Input : A 3,A 4,B,S,S,S,S,S,B
1
2

'''
# class Stack :
#     def __init__(self , list = None):
#         if list == None :
#             self.items = []
#         else :
#             self.items = list
#     def __str__(self) -> str:
#         s = f"stack of {str(self.size())} items :"
#         for element in self.items :
#             s += f"{str(element)} "
#         return s
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         try :
#            return self.items[-1]
#         except :
#             return -1
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)


# s1 = Stack()
# mushroom = 0

# list_opt = input("Enter Input : ").split(",")
# for opt in list_opt:
#     action =  opt.split(" ")
#     if action[0]== "A":
#         s1.push(int(action[1]))
#     elif action[0]== "B":
#         s2 = Stack()
#         temp = Stack()
#         if s1.peek() != -1 :
#             temp.push(s1.peek())
#             s2.push(s1.pop())
#             for i in range(s1.size()):
#                 temp.push(s1.peek())
#                 if s2.peek() < s1.peek() :
#                     s2.push(s1.pop())
#                 else :
#                     s1.pop()
#         print(s2.size())
#         for i in range(temp.size()):
#             s1.push(temp.pop())
#     elif action[0]=="S":
#         s2 = Stack()
#         for i in range(s1.size()):
#             if s1.peek() != -1 :
#                 if s1.peek() % 2 != 0 :
#                     s2.push(s1.pop()+2)
#                 else :
#                     s2.push(s1.pop()-1)
#         for i in range(s2.size()):
#             s1.push(s2.pop())




class Stack:
    def __init__(self, list=None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)


stack1 = Stack()

inp = input("Enter Input : ").split(",")
for n in inp:
    ac = n.split(" ")
    symbol = ac[0]

    if symbol == "A":
        stack1.push(int(ac[1]))
    elif symbol == "B":
        stack2 = Stack()   #collect result
        temp = Stack()

        if stack1.peek() != -1:

            temp.push(stack1.peek())
            stack2.push(stack1.pop())

            for x in range(stack1.size()): #len list

                temp.push(stack1.peek())

                if stack2.peek() < stack1.peek():

                    stack2.push(stack1.pop())

                else:
                    stack1.pop()

        print(stack2.size())

        for x in range(temp.size()):

            stack1.push(temp.pop())
    elif symbol == "S":

        stack2 = Stack()

        for x in range(stack1.size()):
            if stack1.peek() != -1:

                if stack1.peek() % 2 != 0:
                    stack2.push(stack1.pop() + 2)

                else:
                    stack2.push(stack1.pop() - 1)

        for x in range(stack2.size()):
            stack1.push(stack2.pop())




