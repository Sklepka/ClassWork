""" # Написать игру "Угадай число"
import random

def random_num():
    x = int(random.randint(1, 100))
    return x

def search_num():
    print('Я загадал число, попробуй его угадать. Введи число: ', end = '')
    input_num = int(input())
    random_num1 = random_num()
    cond = True
    attempts = int(0)
    while cond:
        if input_num == random_num1:
            print('Здорово, ты угадал. На это у тебя ушло - ', attempts, ' попыток.')
            cond = False
        if input_num != random_num1:
            if input_num < random_num1:
                print('Мое число - больше, попробуй еще. Введи число: ', end = '')
                input_num = int(input())
                attempts += 1
            if input_num > random_num1:
                print('Мое число - меньше, попробуй еще. Введи число: ', end = '')
                input_num = int(input())
                attempts += 1

    
search_num() """
""" 
# Написать игру "Виселица"
import random

def random_str():

    slovar = ['Мама', 'День', 'Ночь', 'Свет', 'Фонарь', 'Листок', 'Бумага', 'Дерево', 'Стол', 
    'Стул', 'Книга', 'Журнал', 'Ковер', 'Кровать', 'Матрас', 'Плед', 'Игрушка', 'Телевизор'] # 18 слов
    random_num = random.randint(0, 17)
    slovo = slovar[random_num]

    return slovo

def viselica():

    slovo = list(random_str().lower())
    dlina_slova = len(slovo)
    healts = int(10)
    cond = True
    zag_slovo = list(dlina_slova * '*')
    # print(slovo)
    print('Мы играем в виселицу. Я загадал слово из ', dlina_slova, ' букв. Назови первую букву: ', end = '')


    while cond:
        letter = input().lower()

        if slovo != zag_slovo:
            
            for id, litter in enumerate(slovo):
                if litter == letter and healts > 0:
                    zag_slovo[id] = litter
                    print('Вы угадали букву - ', letter, '. Обновим слово: ', zag_slovo)
                                        
            if letter not in slovo:
                healts -= 1
                print('Такой буквы в слове нет. Количество оставшихся жизней: ', healts, '. Повторите ввод буквы: ')        
            
            if healts == 0:
                print('Вы потратили все попытки, так не угадав слово. Слово было - ', slovo)
                cond = False
        
        if slovo == zag_slovo:
            print('Вы угадали слово - ', slovo, '. Количество оставшихся жизней - ', healts, '.')
            cond = False
        
        print('Введите следующую букву: ', end = '')     
                

                     
viselica() """

# игра 21
""" import random

def random_map():
    koloda = {
        '6 ♥': 6, '7 ♥': 7, '8 ♥': 8, '9 ♥': 9, '10 ♥': 10, 'V ♥': 2, 'D ♥': 3, 'K ♥': 4, 'A ♥': 11, 
        '6 ♦': 6, '7 ♦': 7, '8 ♦': 8, '9 ♦': 9, '10 ♦': 10, 'V ♦': 2, 'D ♦': 3, 'K ♦': 4, 'A ♦': 11, 
        '6 ♣': 6, '7 ♣': 7, '8 ♣': 8, '9 ♣': 9, '10 ♣': 10, 'V ♣': 2, 'D ♣': 3, 'K ♣': 4, 'A ♣': 11, 
        '6 ♠': 6, '7 ♠': 7, '8 ♠': 8, '9 ♠': 9, '10 ♠': 10, 'V ♠': 2, 'D ♠': 3, 'K ♠': 4, 'A ♠': 11, 
        }

    random_map = random.choice(list(koloda.keys()))
    map_point = koloda.get(random_map)
    koloda.pop(random_map)

    print(koloda)
    print(map_point)
    print(random_map)

random_map() """

""" # Игра "крестики-нолики"
def pole():
    poligon = ['___', '|', '___', '|', '___/n', 
            '___', '|', '___', '|', '___/n',
            '   ', '|', '   ', '|', '   ']
        
    print(*poligon)
    # return(print(' ___|___|___\n', '___|___|___\n', '   |   |   '   ))

pole()    
 """

