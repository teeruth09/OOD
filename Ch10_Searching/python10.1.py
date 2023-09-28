'''
Chapter : 10 - item : 1 - หัดใช้ Binary Search
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))


Enter Input : 33 2 11 82 77 28 15 76 9 64/28
True


Enter Input : 33 2 11 82 77 28 15 76 9 64/50
False

'''
def bi_search(l, r, arr, x):
    # Code Here
    if l <= r:
        if arr[l] == x:
            return True
        else:
            return bi_search(l+1,r,arr,x)
    else:
        return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
