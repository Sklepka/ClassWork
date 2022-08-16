# Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError. 
# Обрабатываем ошибку, говорим пользователю, в чем его ошибка
""" def user_input():
    
    try:
        x = int(input())
    except ValueError as e:
        print('Вы ввели не число')

    try:
        if type(x) == int:
            if x % 2 != 0 and x > 0 and x < 10:
                print('Вы ввели нечетное число - ', x)
            if x == 0:
                print('Вы ввели 0, ноль - четное число')
            if x % 2 == 0 and x > 0 and x < 10:
                raise ValueError('Вы ввели четное число')
            elif x < 0:
                raise TypeError('Ваше число меньше нуля')
            elif x > 10:
                raise IndexError('Ваше число больше десяти')
        else: raise Exception('Введите число')
    except ValueError as e:
        print(e)
    except TypeError as e1:
        print(e1)
    except IndexError as e2:
        print(e2)
    except Exception as e3:
        print(e3)

user_input() """


# Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. 
# Если все хорошо - пишите объект в консоль. 
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так
""" def spisok():
    try:    
        List = (0 ,1 ,2, 'three', 'four', 5, 'six', {7: 7}, {8 :8}, None, 0 , -1)
        ind = int(input())
        print(List[ind])
    except IndexError:
        print('Превышен индекс, вы можете ввести число от: -', len(List), 'до: +', len(List) -1)
    except ValueError:
        print('Введенный Вами параметр не соответствует правилам ввода. Вы можете ввести только  целое число')
spisok() """

# Написать функцию, которая принимает на вход два аргумента. 
# Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0
""" def func(x, y):
    try:
        if x >= 0 and y >= 0:
            return x + y
        if x <= 0 and y <= 0:
            return x - y
        else: return 0
    except TypeError as e:
        print('Вы можете вводить только числа')
        return e

print(func(-9, -7)) """

# Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
""" def func(x, y ,z):
    try:
        max_1 = max(x, y, z)
        if max_1 == x:
            max_2 = max(y, z)
        if max_1 == y:
            max_2 = max(x, z)
        if max_1 == z:
            max_2 = max(x, y)
        print('Первое максимальное = ', max_1, '\nВторое максимальное = ', max_2)
    except TypeError:
        print('Вы можете вводить только числа')

func( -1, 1.5, 4) """

# Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка
""" def func(spisok_int, boolean):
    print(spisok_int)
    spisok_new = []
    if boolean == True:
        for num in spisok_int:
            if num % 2 != 0:
                spisok_new.append(num)
        print("\033[33m {}" .format(spisok_new))
    if boolean == False:
        for num in spisok_int:
            if num % 2 == 0:
                spisok_new.append(num)
        print("\033[33m {}" .format(spisok_new))
    
func([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 9, 10, 0, 0], True) """


# Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба
""" def func(*chisla):
    return(max(chisla), min(chisla))

print(func(1, 2, 3, 4, 5, 4, 3, 2, 0)) """


# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему
""" def func(stroka, boolean = True):
    print(stroka)
    if boolean == True:
        return stroka.upper()
    if boolean == False:
        return stroka.lower()

print(func('QWdsdeWEsdaaW', True)) """


# Написать функцию, которая принимает любое количество позиционных аргументов - строк и один параметр по-умолчанию glue, который равен ':'. 
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue
""" def func(*pos_args, glue = ':'):
    new_str = ''
    for i in pos_args:
        if len(pos_args) > 3:
            new_str += str(i) + glue
    return new_str[:-1]

print(func(3, 6, 5, 4, 'str', 'str1', {3:3}, {10:234234},234234, 'i')) """
