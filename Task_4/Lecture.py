""" def my_function():
    print('I am a function')

print(my_function)
print('Functions are objects', isinstance(my_function, object))

test = my_function
test()

my_list = []
my_list.append(my_function)
print(my_list)

def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')

call_passed_function(my_function)


try:
    d = 2
    d()
except TypeError as e:
    print('It is not a function', e)


print(callable(len), callable(45), callable(callable))

def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)  """



""" def pretty_print(arg):
    def print_stars():
        print('-' * 8)
        print('*' * 8)

    print_stars()
    print(arg)
    print_stars()

pretty_print(12) """


""" def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4)) """


""" def print_all_list_items(data):
    if not data:
        return
    item = data.pop()
    print(item)
    return print_all_list_items(data)

print_all_list_items(['1', '2', 'end']) """


""" s, k = (1, 2)
print(s, k)

s, k = [10, 5]
print(s, k)

first, *second = 'My string'
print(first, second)

first, *mid, last = 'some letters'
print(first, mid, last) """


""" def find_min_max(data):
    min_num = min(data)
    max_num = max(data)

    return min_num, max_num

minimum, maximum = find_min_max([1, 9, 0]) """

""" def accepts_args(*args):
    print(args)
    return sum(args)

accepts_args(1, 3, 9, 0)

values = [1, 4, 9, 3]

try:
    accepts_args(values) # так не будет работать
except TypeError as e:
    print('Error', e)

accepts_args(*values) # так будет работать """


""" def accepts_kwargs(**kwargs):
    print(kwargs)

accepts_kwargs(name = 'Nikita', job = 'dev')

values = {'day': 'wed', 'month': 'may'}

try:
    accepts_kwargs(values)
except TypeError as e:
    print('Error', e)

accepts_kwargs(**values) """
