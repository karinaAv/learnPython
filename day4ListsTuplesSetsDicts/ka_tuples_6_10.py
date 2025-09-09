import random
def generate_tuple_with_random_values(list_length: int):
    return tuple(random.randint(0, 10) for _ in range(list_length))

print('6. Объедини два кортежа.')
def join_tuples(*tuples):
    print(tuples)
    return sum(tuples, ())
from itertools import chain

def join_tuples1(*tuples):
    print(tuples)
    return tuple(chain.from_iterable(tuples))

print(f'result 1: {join_tuples(
    generate_tuple_with_random_values(3),
    generate_tuple_with_random_values(5),
    generate_tuple_with_random_values(2)
)}')

print(f'result 2: {join_tuples1(
    generate_tuple_with_random_values(3),
    generate_tuple_with_random_values(5),
    generate_tuple_with_random_values(2)
)}'
)

print('7. Найди индекс заданного элемента.')
def get_element_index(tup, elem):
    return tup.index(elem)

random_tup = generate_tuple_with_random_values(8)
print(random_tup)
el = int(input('Enter element: '))
print(get_element_index(random_tup, el))

print('8. Создай кортеж из повторяющихся значений и посчитай количество вхождений.')
def count_occurrences(tup, element):
    return tup.count(element)

tuple_with_el = generate_tuple_with_random_values(20)
print(tuple_with_el)
el = int(input('Enter element: '))
print(count_occurrences(tuple_with_el, el))

print('9. Создай вложенный кортеж и выведи элемент из внутреннего кортежа.')
tuple_with_el = (1, 2, 3, (7, 8, (9, 0)))
print(tuple_with_el[1]) #2
print(tuple_with_el[3][1]) #8
print(tuple_with_el[3][2][1]) #0
print(tuple_with_el[-1][-1][0]) #9

print('10. Раздели кортеж на две части.')
def split_tuple(tup):
    mid = len(tup) // 2
    return tup[:mid], tup[mid:]

n = int(input('Enter tuple len: '))
tuple_with_el = generate_tuple_with_random_values(n)
print(split_tuple(tuple_with_el))
