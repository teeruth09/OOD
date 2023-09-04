'''
นับเกาะ 

มี map โดยที่ เลข 0 เป็นน้ำทะเล เลข 1 เป็นพื้นดิน จงหาว่าใน map มีกี่เกาะถ้าพื้นดินติดกันซ้าย ขวา บน ล่าง ถือว่าเป็นเกาะเดียวกัน

เช่น

0001

1100

0010

จะมี3เกาะ

*** ให้เขียนcode ในฟังก์ชั่น เท่านั้น ***

def deleteIsland(Map,y,x):

    pass

def countIsland(Map):

    pass

Input = input("Enter Input : ").split('/')

Map=[]

for i in Input:

    temp=[*i]

    temp = list(map(int,temp))

    Map.append(temp)

print(f"Island have : {countIsland(Map)}")

Enter Input : 001/100/010
Island have : 3


Enter Input : 0000/0000/0000
Island have : 0


Enter Input : 000/010/000
Island have : 1

'''
def deleteIsland(Map,y,x):
    if y < 0 or x < 0 or y >= len(Map) or x >= len(Map[y]) or Map[y][x] == 0:
        return Map
    Map[y][x] = 0
    Map = deleteIsland(Map,y,x-1)
    Map = deleteIsland(Map,y,x+1)
    Map = deleteIsland(Map,y-1,x)
    Map = deleteIsland(Map,y+1,x)
    return Map 

def countIsland(Map):
    count = 0 
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if Map[i][j] == 1:
                count += 1
                Map = deleteIsland(Map,i,j)
                
    return count    

Input = input("Enter Input : ").split('/')

Map=[]

for i in Input:

    temp=[*i]

    temp = list(map(int,temp))

    Map.append(temp)

print(f"Island have : {countIsland(Map)}")