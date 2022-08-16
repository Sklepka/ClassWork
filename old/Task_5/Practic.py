# *ЗАДАЧА 1:
# 1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
# В объекты класса корзина можно помещать разные объекты;
# 2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
# 3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
# 4. Если вместимости недостаточно, сказать, что объект поместить нельзя.

""" class Basket(object):
    def __init__(self, size):
        self.size = size
    
    def print_size(self):
        print('Размер корзины = ', self.size)

    def comparison(self, obj):
        if obj.size <= self.size:
            print('Размер коробки больше размера корзины')
        else:
            print('Коробка помещена в корзину')

class Package(Basket):
    def print_size(self, size):
        print('Размер пакета = ', self.size)

    def comparison(self, obj):
        if obj.size <= self.size:
            print('Размер коробки больше размера пакета')
        else:
            print('Коробка помещена в пакет')
    
class Bag(object):
    def __init__(self, size):
        self.size = size
    
    def print_size(self):
        print('Размер коробки = ', self.size)

bag1 = Bag(20)
bag2 = Bag(10)
bag3 = Bag(5)

basket1 = Basket(10)
basket2 = Basket(20)
basket3 = Basket(30)    

package1 = Package(10)
package2 = Package(20)
package3 = Package(30)  

basket1.print_size()
basket2.print_size()
basket3.print_size()

bag1.print_size()
bag2.print_size()
bag3.print_size()

basket1.comparison(bag1)
basket2.comparison(bag2)
basket3.comparison(bag3) """


# *ЗАДАЧА 2:
# Пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник

class Square(): # квадрат
    def print_square(self): 
        print(' __\n|  |\n ¯¯')

class Rectangle(): # прямоугольник
    def print_rectangle(self): 
        print(' ______\n|      |\n ¯¯¯¯¯¯')

class Triangle(): # треугольник
    def print_triangle(self): 
        print(' /\\\n/  \\\n¯¯¯¯')
    
class Polygon(): # многоугольник
    def print_polygon(self): 
        print(' ___\n/   \\\n\\   /\n ¯¯¯')

square1 = Square()
rectangle1 = Rectangle()
triangle1 = Triangle()
polygon1 = Polygon()

def user_input():
    x = input('Введите число от 1 до 4: ')
    return x

def func():
    match user_input():
        case '1':
            square1.print_square()
        case '2':
            rectangle1.print_rectangle()
        case '3':
            triangle1.print_triangle()
        case '4':
            polygon1.print_polygon()                        

func()            