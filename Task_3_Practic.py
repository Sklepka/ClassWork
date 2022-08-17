# Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или RuntimeError случайным образом.

""" import random

def proverka():
    number = random.randint(1, 3)
    print('Случайное число - ', number)
    if number == 1:
        try:
            raise ValueError('Получили - ValueError')
        except ValueError as e:
            print(e)
    if number == 2:
        try:
            raise TypeError('Получили - TypeError')
        except TypeError as e:
            print(e)
    if number == 3:
        try:
            raise RuntimeError('Получили - RuntimeError')
        except RuntimeError as e:
            print(e)
             
proverka() """

# В месте вызова функции обрабатывать все три исключения
""" import random

def proverka():
    number = random.randint(1, 3)
    print('Случайное число - ', number)
    if number == 1:
        raise ValueError('ValueError')
    if number == 2:
        raise TypeError('TypeError')
    if number == 3:
        raise RuntimeError('RuntimeError')
             
try:
    proverka()
except ValueError as e:
    print('Наша ошибка - ', e)
except TypeError as e:
    print('Наша ошибка - ', e)
except RuntimeError as e:
    print('Наша ошибка - ', e) """

# Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError.
""" def test(*args):
    test_1 = []
    lenght = len(args)
    num = 0
    for i in range(lenght):
        if type(args[i]) == int:
            test_1.append(args[i])
            num += 1
    try:
        if num == lenght:
            test_1.sort()
            print(test_1)
        if num != lenght:
            raise ValueError('Неверный ввод')
    except ValueError as e:
        print(e)
   
test(9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2) """

# Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь
""" def test(args):
    new = dict()
    for key, value in args.items():
        new[str(key)] = value
    print(new)
    return new

test({4:1, 3:2, 'stre':45, 5:5}) """

# Написать функцию, которая принимает список чисел и возвращает их произведение
""" def test(*args):
    proizvedenie = 1
    try:
        for i in args:
            if type(i) == int:
                proizvedenie *= i
            elif type(i) != int:
                raise TypeError('Неверный ввод. Введите только числа')
        print(proizvedenie)
    except TypeError as e:
        print(e)
    return proizvedenie
test(5, 3, 2, 2, 2, 5, 1, 'str') """


# Написать функцию которая проверяет наличие букв одного листа в другом
""" def func(a):
    c = []
    i = 0
    for ch in a:
        if ch not in c:
            c.append(ch)
    for ch in c:
        i += 1
    return(i)

func([0, 1, 0, 2, 0, 1, 2, 2 ,2 ,3]) """

