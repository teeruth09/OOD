'''
รับข้อความ 2 ข้อความ

ข้อความแรกให้หมุนซ้าย ข้อความที่สองให้หมุนขวา

แสดงผล

หยุดเมื่อข้อความที่หมุน เหมือนข้อความที่รับเข้ามา

โดยแสดงผล 5 บรรทัดแรก และบรรทัดสุดท้าย

*** String Rotation ***
Enter 2 strings : 123 456
1 312 564
2 231 645
3 123 456
Total of  3 rounds.

*** String Rotation ***
Enter 2 strings : dict dept
1 tdic eptd
2 ctdi ptde
3 ictd tdep
4 dict dept
Total of  4 rounds.

*** String Rotation ***
Enter 2 strings : Marvel Stinger
1 lMarve tingerS
2 elMarv ingerSt
3 velMar ngerSti
4 rvelMa gerStin
5 arvelM erSting
 . . . . . 
42 Marvel Stinger
Total of  42 rounds.

*** String Rotation ***
Enter 2 strings : debate string
1 edebat trings
2 tedeba ringst
3 atedeb ingstr
4 batede ngstri
5 ebated gstrin
6 debate string
Total of  6 rounds.

*** String Rotation ***
Enter 2 strings : jukebox hijacks
1 xjukebo ijacksh
2 oxjukeb jackshi
3 boxjuke ackshij
4 eboxjuk ckshija
5 keboxju kshijac
 . . . . . 
7 jukebox hijacks
Total of  7 rounds.

*** String Rotation ***
Enter 2 strings : King Mongkut
1 gKin ongkutM
2 ngKi ngkutMo
3 ingK gkutMon
4 King kutMong
5 gKin utMongk
 . . . . . 
28 King Mongkut
Total of  28 rounds.

*** String Rotation ***
Enter 2 strings : aaaaaaa 123123
1 aaaaaaa 231231
2 aaaaaaa 312312
3 aaaaaaa 123123
Total of  3 rounds.

*** String Rotation ***
Enter 2 strings : Molnupiravir Outpatients
1 rMolnupiravi utpatientsO
2 irMolnupirav tpatientsOu
3 virMolnupira patientsOut
4 avirMolnupir atientsOutp
5 ravirMolnupi tientsOutpa
 . . . . . 
132 Molnupiravir Outpatients
Total of  132 rounds.

'''

def left_rotate_string(string):
    return string[1:] + string[0]

def right_rotate_string(string):
    return string[-1] + string[:-1]

def rotate_strings(string1, string2):
    round = 0
    temp1 = string1
    temp2 = string2
    while not (temp1 == string1 and temp2 == string2 and round != 0):
        round += 1
        temp1 = right_rotate_string(temp1)
        temp2 = left_rotate_string(temp2)

        if round == 7:
            print(' . . . . . ')
        elif round <= 5:
            print(round, temp1, temp2)

        if temp1 == string1 and temp2 == string2:
            if round > 5:
                print(round, temp1, temp2)
            break
        
    print(f'Total of  {round} rounds.')
    return round


print("*** String Rotation ***")
string1, string2 = [x for x in input("Enter 2 strings : ").split()]
rotate_strings(string1, string2)
