import random
def generate_list_with_random_values(list_length: int):
    return [random.randint(0, 100) for _ in range(list_length)]

print('11. Проверь, является ли список палиндромом.')
def is_palindrome1(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(random_list)
    return random_list == random_list[::-1]

def is_palindrome2():
    random_list = list(range(1, 4)) + list(range(3, 0, -1))
    print(random_list)
    is_palindrome = True
    for i in range(len(random_list) // 2):
        if random_list[i] != random_list[-i - 1]:
            is_palindrome = False
            break
    return is_palindrome

n = int(input('Enter length of the list N: '))
print(f'Is palindrome {is_palindrome1(n)}')
print(f'Is palindrome {is_palindrome2()}')

print('12. Посчитай, сколько раз каждый элемент встречается в списке.')
from collections import Counter

def get_number_of_entries():
    random_list = list(range(0, 5)) + list(range(3, 0, -1))
    return dict(Counter(random_list))

def get_number_of_entries1():
    random_list = list(range(0, 5)) + list(range(3, 0, -1))
    entries_dict = {}
    for num in random_list:
        entries_dict[num] = entries_dict.get(num, 0) + 1
    return entries_dict

print(f'Number of entries of {get_number_of_entries()}')
print(f'Number of entries of {get_number_of_entries1()}')

print('13. Найди пересечение двух списков (общие элементы).')
def check_intersection():
    first_list = list(range(0, 5)) + list(range(3, 0, -1))
    print(first_list)
    second_list = list(range(1, 3)) + list(range(5, 3, -1))
    print(second_list)
    return list(set(first_list) & set(second_list))

def check_intersection1():
    first_list = list(range(0, 5)) + list(range(3, 0, -1))
    print(first_list)
    second_list = list(range(1, 3)) + list(range(5, 3, -1))
    print(second_list)
    return [num for num in first_list if num in second_list]

def check_intersection2():
    first_list = list(range(0, 5)) + list(range(3, 0, -1))
    print(first_list)
    second_list = list(range(1, 3)) + list(range(5, 3, -1))
    print(second_list)
    set_for_second_list = set(second_list)
    return [num for num in first_list if num in set_for_second_list]

print('Intersection of lists ', check_intersection())
print('Intersection of lists ', check_intersection1())
print('Intersection of lists ', check_intersection2())

print('14. Найди подсписок с максимальной суммой (задача "maximum subarray").')
def max_subarray(list_length):
    random_list = generate_list_with_random_values(list_length)
    max_sum = random_list[0]
    current_sum = random_list[0]
# [10, 20, 10, 50] max_sum = 10, current_sum = 10
    for num in random_list[1:]: #
        current_sum = max(num, current_sum + num) #current_sum = max(50, 10 + 40) = 50
        max_sum = max(max_sum, current_sum) # max_sum = max(50, 50) = 50

    return max_sum

def max_subarray_with_list(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(random_list)
    max_sum = random_list[0]
    current_sum = random_list[0]
    start = end = 0
    temp_start = 0
    # [10, 20, 10, 30] max_sum = 10, current_sum = 10
    for i in range(1, list_length):
        if random_list[i] > current_sum + random_list[i]: #
            current_sum = random_list[i]
            temp_start = i
        else:
            current_sum += random_list[i]# current_sum = 40 + 30 = 70

        if current_sum > max_sum: #40 > 10
            max_sum = current_sum # 70
            start = temp_start # 0
            end = i # 3

    return max_sum, random_list[start:end + 1] #70, random_list[0:4]=[10, 20, 10, 30]

def max_subarray_bruteforce(list_length):
    random_list = generate_list_with_random_values(list_length)
    max_sum = random_list[0]
    best_subarray = [random_list[0]]

    for i in range(list_length):
        current_sum = 0
        for j in range(i, list_length):
            current_sum += random_list[j]
            if current_sum > max_sum:
                max_sum = current_sum
                best_subarray = random_list[i:j + 1]

    return max_sum, best_subarray

n = int(input('Enter length of the list N: '))
print(f'Алгоритм Кадане (O(n), оптимальный) {max_subarray(n)}')
print(f'Хранение самого подсписка {max_subarray_with_list(n)}')
print(f'Брутфорс (O(n²), для понимания) {max_subarray_bruteforce(n)}')


print('15. Реализуй алгоритм сортировки списка без встроенных функций (например, пузырьком или вставками).')
def bubble_sort(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(f'Before buble sort {random_list}')
    # [20, 10, 30, 5]
    for i in range(list_length):
        for j in range(0, list_length - i - 1):# (0, 3) i=0
            if random_list[j] > random_list[j + 1]:
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j] #кортежное присвоение!
    return random_list

def insertion_sort(list_length):
    random_list = generate_list_with_random_values(list_length)
    print(f'Before insertion sort {random_list}')
    for i in range(1, list_length):
        key = random_list[i]
        j = i - 1
        while j >= 0 and random_list[j] > key:
            random_list[j + 1] = random_list[j]
            j -= 1
        random_list[j + 1] = key
    return random_list

n = int(input('Enter length of the list N: '))
print(f'After buble sort {bubble_sort(n)}')
print(f'After insertion sort {insertion_sort(n)}')
