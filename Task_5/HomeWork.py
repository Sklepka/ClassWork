""" class Person(object):

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.spisok = []

    def know(self, person):
        self.spisok.append(person)

    def is_known(self, person):
        for name1 in self.spisok:
            if name1 == person:
                print(self.name, 'знаком c', person+'ом')
            elif name1 != person:
                print(self.name, 'не знаком c', person+'ом')

Ivan = Person(32, 'Иван')
Ivan.know('Ильяс')
Ivan.is_known('Ильяс')
Ivan.is_known('Петр') """

""" class Animal(object):

    def __init__(self, name, danger, kind):
        self.name = name
        self.danger = danger
        self.kind = kind

class Human(object):

    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina

    def is_dangerous(self, animal):
        if animal.kind == 'Травоядное':
            if animal.danger > self.stamina:
                print(animal.name,'опасен для', self.name+'a',', потому что угроза',animal.name.lower(),'выше, чем выносливость', self.name)
            elif animal.danger <= self.stamina:
                print(animal.name,'не опасен для', self.name+'a')
        elif animal.kind == 'Ядовитое' or 'Хищник':
            print(animal.name,'опасен для', self.name+'a',', потому что',animal.name.lower(),'-', animal.kind.lower())

Bear = Animal('Медведь', 4, 'Хищник')
Rabbit = Animal('Кролик', 1, 'Травоядное')
Elepfant = Animal('Слон', 4, 'Травоядное')
Cobra = Animal('Кобра', 5, 'Ядовитое')
Ivan = Human('Иван', 3)
Ivan.is_dangerous(Bear)
Ivan.is_dangerous(Rabbit)
Ivan.is_dangerous(Elepfant)
Ivan.is_dangerous(Cobra)
 """

""" class Printer(object):

    def log(*values):
        print(*values)

class FormattedPrinter(Printer):

    def log(*values):
        for str in values:
            print('*',str,'*')
spisok = Printer()
spisok.log(1,2,3,4,5,6,67)
spisok1 = FormattedPrinter()
spisok1.log(1,2,3,4,5,6,67) """




class Figure(object):

    def __init__(self, *value):
        length = len(value)
        match length:
            case 1:
                self.f = Square(*value)
            case 2:
                self.f = Rectangle(*value)
            case 3:
                self.f = Triangle(*value)
            case 4:
                self.f = Polygon(*value)                                
            case default:
                return print('Вы ввели больше чисел')
    
    def perimeter(self):
        return self.f.perimeter()
    
    def area(self):
        return self.f.area()

class Square():

    def __init__(self, *value):
        self.a = value[0]

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2


class Rectangle():

    def __init__(self, *value):
        self.a = value[0]
        self.b = value[1]

    def perimeter(self):
        return (self.a +self.b) * 2

    def area(self):
        return self.a * self.b


class Triangle():

    def __init__(self, *value):
        self.a = value[0]
        self.b = value[1]
        self.c = value[2]

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = ((self.a + self.b + self.c) / 2)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Polygon():

    def __init__(self, *value):
        self.a = value[0]
        self.b = value[1]
        self.c = value[2]
        self.d = value[3]

    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def area(self):
        p = ((self.a + self.b + self.c) / 2)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

print(Figure(2,2,6).perimeter())







                
    