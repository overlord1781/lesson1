v = (input('Введите число от 1 до 10 '))
if type(v) == int and v>=1 and v<=10:
    print(v+10)
else: 
    print('Вы ввели не верное число')