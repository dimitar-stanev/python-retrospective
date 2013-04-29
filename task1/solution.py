ARIES = (range(21, 32), 3), (range(1, 20), 4), 'Овен'
TAURUS = (range(20, 32), 4), (range(1, 21), 5), 'Телец'
GEMINI = (range(21, 32), 5), (range(1, 21), 6), 'Близнаци'
CANCER = (range(21, 32), 6), (range(1, 23), 7), 'Рак'
LEO = (range(23, 32), 7), (range(1, 23), 8), 'Лъв'
VIRGO = (range(23, 32), 8), (range(1, 23), 9), 'Дева'
LIBRA = (range(23, 32), 9), (range(1, 23), 10), 'Везни'
SCORPIO = (range(23, 32), 10), (range(1, 22), 11), 'Скорпион'
SAGGITARIUS = (range(22, 32), 11), (range(1, 22), 12), 'Стрелец'
CAPRICORN = (range(22, 32), 12), (range(1, 20), 1), 'Козирог'
AQUARIUS = (range(20, 32), 1), (range(1, 19), 2), 'Водолей'
PISCES = (range(20, 32), 2), (range(1, 21), 3), 'Риби'

ALL_SIGNS = {ARIES, TAURUS, GEMINI, CANCER, LEO, VIRGO, LIBRA, SCORPIO,
             SAGGITARIUS, CAPRICORN, AQUARIUS, PISCES}


def what_is_my_sign(day, month):
    for sign in ALL_SIGNS:
        if ((month == sign[0][1] and day in sign[0][0] or
        	 month == sign[1][1] and day in sign[1][0])):
            return sign[2]
