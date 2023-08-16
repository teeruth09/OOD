'''
Chocolate wrapper

น้องมีเงิน m บาท ช็อกโกแลตราคา p บาท ร้านค้ามีนโยบายว่าสามารถนำที่ห่อช็อกโกแลต w แผ่น
จงหาว่าน้องสามารถกินช็อกโกแลตสูงสุดได้กี่ชิ้น

Input: money = 16, price = 2, wrap = 2
Output:   15
ตอนแรกมีเงิน 16 บาท ช็อกโกแลตราคา 2 บาท ก็จะสามารถซื้อได้ 8 ชิ้น นำที่ห่อช็อกโกแลต 8 แผ่นมาแลกช็อกโกแลตได้อีก 4 ชิ้นแล้วก็นำที่ห่อช็อกโกแลต 4 แผ่นมาแลกช็อกโกแลตได้ 2 ชิ้น สุดท้ายก็นำที่ห่อช็อกโกแลต 2 แผ่นมาแลกช็อกโกแลต 1 ชิ้น
8 + 4 + 2 + 1 = 15

Enter m, p, w: 16 2 2
15

Enter m, p, w: 15 1 3
22

Enter m, p, w: 20 3 5
7
'''


inp = input("Enter m, p, w: ").split()
money = int(inp[0])
price = int(inp[1])
wrap = int(inp[2]) #จำนวนห่อที่ใช้ต่อการแลกเปลี่ยน1 ชิ้น 

def buy(money,price):
    piece = money // price
    return piece

piece = buy(money,price)
total = piece
def exchange_package(total,piece,wrap):
    total = total
    if piece // wrap > 0:
        if piece > 1:
            after_exchange = piece // wrap
            total += after_exchange
            after_exchange += piece % wrap #กรณีมีเศษเหลือ
            return exchange_package(total,after_exchange,wrap)
    else:
        return total
if money > 0 and wrap > 0:
    print(exchange_package(total,piece,wrap))