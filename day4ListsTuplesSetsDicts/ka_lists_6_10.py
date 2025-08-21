import random
def generate_list_with_random_values(list_length: int):
    return [random.randint(0, 100) for _ in range(list_length)]

# 6. Отсортируй список по возрастанию и убыванию.
print('6. Отсортируй список по возрастанию и убыванию.')
def sort_asc(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(randon_list)
    randon_list.sort()
    return randon_list

def sort_desc(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(randon_list)
    randon_list.reverse()
    return randon_list

n = int(input('Enter length of the list N: '))
print(f'ASC: {sort_asc(n)}')
print(f'DESC: {sort_desc(n)}')

# 7. Выведи второй по величине элемент.
print('7. Выведи второй по величине элемент.')
def get_second_max_element(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(randon_list)
    return sorted(randon_list)[-2] #retrun sorted(randon_list, reverse=True)[1]

n = int(input('Enter length of the list N: '))
print(get_second_max_element(n))

# 8. Сдвинь список на 1 элемент вправо (циклический сдвиг).
print('8. Сдвинь список на 1 элемент вправо (циклический сдвиг).')
def move_element(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(f'List: {randon_list}')
    shifted = randon_list[-1:] + randon_list[:-1]
    return shifted

def move_element1(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(f'List: {randon_list}')
    last_element = randon_list.pop()
    randon_list.insert(0, last_element)
    return randon_list

from collections import deque
def move_element2(list_length):
    randon_list = deque(generate_list_with_random_values(list_length))
    print(f'List: {randon_list}')
    randon_list.rotate(1)  # сдвигаем вправо на 1
    return list(randon_list)

n = int(input('Enter length of the list N: '))
print(move_element(n))
print(move_element1(n))
print(move_element2(n))

# 9. Объедини два списка в один, убрав повторяющиеся элементы.
print('9. Объедини два списка в один, убрав повторяющиеся элементы.')
def join_two_lists(list_length):
    first_list = list(range(0, list_length))
    print(f'List: {first_list}')
    second_list = list(range(3, 3+list_length))
    print(f'List: {second_list}')
    first_list.extend(second_list)
    return list(set(first_list))

n = int(input('Enter length of the list N: '))
print(join_two_lists(n))

# 10. Раздели список чисел на два списка: чётные и нечётные.
print('10. Раздели список чисел на два списка: чётные и нечётные.')
def split_list_to_even_odd(list_length):
    randon_list = generate_list_with_random_values(list_length)
    print(f'List: {randon_list}')
    return [
        list(even_num for even_num in randon_list if even_num % 2 == 0),
        list(odd_num for odd_num in randon_list if odd_num % 2 != 0)
    ]

n = int(input('Enter length of the list N: '))
splitted_list = split_list_to_even_odd(n)
print("Чётные:", splitted_list[0])
print("Нечётные:", splitted_list[1])
