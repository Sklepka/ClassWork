# Проверяем вводимое значение на ошибки
""" try:
    1 / int(input('x: '))
except ZeroDivisionError:
    print('Нельзя делить на ноль')
except TypeError:
    print('Неправильный тип данных')
except ValueError:
    print('Неверное значение') """

# Проверяем на ошибку, если есть - записываем в переменную
""" try:
    print(1/0)
except ZeroDivisionError as e:
    print('Eception! Stop it!')
    print(e)
 """

# Создаем ошибку
""" raise IndexError('Hi!') """

# Создаем ошибку и обрабатываем ее
""" from multiprocessing.sharedctypes import Value


try:
    raise TypeError('Some message')
except TypeError as e:
    print(e) """

# try - except - else
""" try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else срабывает в случае, когда ошибки нет') """

# try - except - finally
""" try:
    print(1/0)
except ZeroDivisionError:
    print('0!')
finally:
    print('finally срабыватывает всегда') """

# try - except - else - finally
""" try:
    print('try')
except ValueError:
    pass # pass -  пропускает ошибку, никогда так не делать
else:
    print('else')
finally:
    print('finally') """

# try - finally
""" try:
    raise ValueError()
finally:
    print('Finally') """