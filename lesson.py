def gcd(a,b):

    while a != 0 and b != 0:

        if a > b:

            a = a % b
            a_1 = a
            b_1 = b
            ab = a_1 + b_1
        else:

            b = b % a
            a_1 = a
            b_1 = b
            ab = a_1 + b_1
    print('Наибольший общий делитель:', a + b)
number_1 = int(input('Введите число'))
number_2 = int(input('Введите число'))
gcd(a,b)
