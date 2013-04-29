# coding: utf-8

import os
import sys

Aries = (range(21, 32),3) , (range(1, 20), 4), 'Овен'
Taurus = (range(20, 32),4) , (range(1, 21), 5), 'Телец'
Gemini = (range(21, 32),5) , (range(1, 21), 6), 'Близнаци'
Cancer = (range(21, 32),6) , (range(1, 23), 7), 'Рак'
Leo = (range(23, 32),7) , (range(1, 23), 8), 'Лъв'
Virgo = (range(23, 32),8) , (range(1, 23), 9), 'Дева'
Libra = (range(23, 32),9) , (range(1, 23), 10), 'Везни'
Scorpio = (range(23, 32),10) , (range(1, 22), 11), 'Скорпион'
Sagittarius = (range(22, 32),11) , (range(1, 22), 12), 'Стрелец'
Capricorn = (range(22, 32),12) , (range(1, 20), 1), 'Козирог'
Aquarius = (range(20, 32),1) , (range(1, 19), 2), 'Водолей'
Pisces = (range(20, 32),2) , (range(1, 21), 3), 'Риби'

signs = Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces

def what_is_my_sign(day, month):
    for sign in signs:
        if month == sign[0][1] and day in sign[0][0] or month == sign[1][1] and day in sign[1][0]:
            print(sign[2])
            return sign[2]

 # This is the test data, to ensure my program works correctly.
 #what_is_my_sign(5, 8)
 #what_is_my_sign(29, 1)
 #what_is_my_sign(30, 6)
 #what_is_my_sign(31, 5)
 #what_is_my_sign(2, 2)
 #what_is_my_sign(month=5, day=8)
 #what_is_my_sign(9, month=1)
