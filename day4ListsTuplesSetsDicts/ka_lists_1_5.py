# 1. Создай список из 10 чисел и выведи их сумму.
print('Создай список из 10 чисел и выведи их сумму.')
def get_sum_list_n(l: int):
    list_num = range(1, l + 1)
    print(f'list {list(list_num)}')
    return sum(num for num in range(1, l + 1))
n = int(input('Enter length of the list N: '))
print(get_sum_list_n(n))

# 2. Найди максимальное и минимальное значение в списке.
print('Найди максимальное и минимальное значение в списке.')
import random
def generate_list_with_random_values(list_length: int):
    return [random.randint(0, 100000) for _ in range(list_length)]

def get_max_min_from_list(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(f'list {random_list}')
    return [max(random_list), min(random_list)]

n = int(input('Enter length of the list: '))
print(get_max_min_from_list(n))

# 3. Посчитай количество чётных чисел в списке.
print('Посчитай количество чётных чисел в списке.')

def get_count_even_numbers(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(f'list {random_list}')
    return sum(1 for number in random_list if number % 2 == 0)

n = int(input('Enter length of the list: '))
print(get_count_even_numbers(n))

# 4. Разверни список в обратном порядке (без использования [::-1]).
print('Разверни список в обратном порядке (без использования [::-1]).')

def reverse_list(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(f'list {random_list}')
    return list(reversed(random_list))

n = int(input('Enter length of the list: '))
print(reverse_list(n))
# 5. Найди индекс первого вхождения заданного элемента.
print('Найди индекс первого вхождения заданного элемента.')

def get_index_of_first_element_entry(element, list_length):
    random_list = list(range(0, list_length))
    print(f'list {random_list}')
    return random_list.index(element)

n = int(input('Enter length of the list: '))
elem = int(input('Enter length of the list: '))
print(get_index_of_first_element_entry(elem, n))
