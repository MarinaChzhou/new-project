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
while True:
   number_1 = int(input('Введите первое число: '))
   number_2 = int(input('Введите второе  число: '))
   gcd(number_1,number_2)
   switch = int(input('Продолжим? Да/1; Нет/0 : ' ))
   

