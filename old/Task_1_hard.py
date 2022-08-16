# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
""" 
from audioop import reverse

List = [1, 2, 3, 5, 4, 3, 2, 1]
List.sort(reverse=False)
print(List)
 """

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
""" dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

for i, j in dict1.items():
    print (i,' - ',j)
 """

# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
""" turple = (1.1, 2.2, 1.3, 1.4, 5.5, 6.6, 7.7, 2.3, 1.4, 5.1,)
print (max(turple), ' - max', min(turple), ' - min') """

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'
""" List = ['Earth', 'Russia', 'Moscow']
List_new = List[0] + ' -> ' + List[1] + ' -> ' + List[2]
print(List_new) """

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
""" Str = '/bin:/usr/bin:/usr/local/bin'
List = list(Str.split(':'))

print(List) """

# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
""" i = list(range(7, 100, 7))
print(i) """

# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
""" List = [ ]
List_1 = []
n = int(0)
j = int(0)

Matrix = [
    (7, 3, 5, 9), 
    (5, 3, 4, 8), 
    (9, 7, 2, 1)
    ]

for str in Matrix:
    print(str)

for i in list(range(0,4)):
    for str in Matrix:
        List.append(str[i])

for i in range(1, 5):
    List_1.append(List[j:j+3])
    j += 3

for i in List_1:
    print(i) """

# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
""" Matrix = [
    (7, 3, 5, 9), 
    (5, 3, 4, 8), 
    (9, 7, 2, 1)
    ]
i = 0

for str in Matrix:
    print(str)

for i in list(range(0,4)):
    for str in Matrix:
        print(str[i]) """


# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
""" List = [0, 'one', 2, 'Three', 4, 'five', {6: 6}, None]
for num in range(len(List)):
    print('Index: ', num, ', Object: ', List[num]) """


# Создать словарь любых объектов, в цикле напечатать в консоль: объект и его индекс
""" Dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
for ind in Dict:
    print('Key: ', ind, ', Item: ', Dict.get(ind)) """


# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
""" List = ['to-delete', 'one', 2, 'to-delete', 4, 'to-delete', {6: 6}, None]
List_1 = []

for num in range(len(List)):
    if List[num] != 'to-delete':
            List_1.append(List[num])

List = List_1
del List_1

print(List) """


# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
""" for i in reversed(range(11)):
    print(i, end = ' ') """