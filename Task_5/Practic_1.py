""" class Car:
    pass

c = Car()
print(c, type(c)) """

""" class Room:
    number = 'Room 34'
    floor = 4

r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor) """

class Door:
    def open(self):
        print('self is', self)
        print('Door is opened!')
        self.opened = True

d = Door()
b = Door()
d.open()
b.open()
print(d)
print(b)