# функция суммы
""" def sum(n1, n2, n3):
    return n1 +n2 +n3

test = sum(1,2,3)
print(test) """

# функция вывода звездочек
""" def this_functions_prints_starts():
    print('I will print stars!')
    print('**********')
this_functions_prints_starts """

# функция суммы двух чисел
""" def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2
first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call) """

# функция без return ворачивает None
""" def my_function(var1, var2, var3):
    print("No way I'm using this: {}, {}, {}".format(var1, var2 ,var3))

new_call = my_function(1, 2, 3) 
print(new_call) """

# функция со позиционными аргументами
""" def with_default(name='Nikita'):
    print('Hello', name)

with_default()
with_default('Artem')
with_default('Alena') """

# функциия с вводимым значением и значением по умолчанию
""" def with_many(pos, default_arg='some'):
    print(pos, default_arg)

with_many(9, 'm') # выдаст 9 и введенный аргумент м
with_many(9) # выдаст 9 и аргумент по умолчанию some
with_many() #выдаст ошибку """

# функция с любым количеством позиционных аргументов
""" def sum_all(*numbers):   # делает список
    suma = sum(numbers)
    print(suma)
    return suma
    
sum_all(1)
sum_all(1, 2, 3, 4, 5, 6, 7, 8) """

# функция с любым количеством keyword-аргументов
""" def any_keywords(**kwargs):    # делает словарь
    print(kwargs, type(kwargs))

any_keywords(k = 1, some = 2, wo = 3)
 """