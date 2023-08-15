'''
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

def mod_position(arr, s):
    //Code Here

Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา

Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 

*** Mod Position ***
Enter Input : ABCDEGFDFDF,5
['E', 'D']

*** Mod Position ***
Enter Input : BANANANABOAT,3
['N', 'A', 'B', 'T']

*** Mod Position ***
Enter Input : iloveKMITL,1
['i', 'l', 'o', 'v', 'e', 'K', 'M', 'I', 'T', 'L']

*** Mod Position ***
Enter Input : ILOVEDATASTRUCTUREANDALGORITHM,2
['L', 'V', 'D', 'T', 'S', 'R', 'C', 'U', 'E', 'N', 'A', 'G', 'R', 'T', 'M']

'''
print("*** Mod Position ***")
result = []
def mod_position(arr, s):
    #write code here 
    for i in range(1,len(arr)+1):
        #print(i)
        if i % s == 0:
            
            #print(arr[i-1])
            result.append(arr[i-1])
        else:
            continue
    return result

arr,s = input("Enter Input : ").split(",")
print(mod_position(arr, int(s)))
