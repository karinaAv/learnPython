# 1. Создай список из 10 чисел и выведи их сумму.
def create_list_and_print_sum() -> int:
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(new_list))


create_list_and_print_sum()


# 2. Найди максимальное и минимальное значение в списке.
def find_max_and_min(new_list: list) -> list:
    max_and_min = [max(new_list), min(new_list)]
    return max_and_min


print(find_max_and_min(new_list=[5, 8, 1, -10, 55]))


# 3. Посчитай количество чётных чисел в списке.
def count_even_numbers_basic(new_list: list) -> int:
    even_numbers = []
    for number in new_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return len(even_numbers)


print(count_even_numbers_basic(new_list=[1, 3, -4, 2, 55]))


def count_even_numbers_advanced(new_list: list[int]) -> int:
    return sum(1 for num in new_list if num % 2 == 0)


print(count_even_numbers_advanced(new_list=[2, 4, 5, 6]))


# 4. Разверни список в обратном порядке (без использования [::-1]).
def reverse_list_basic(new_list: list) -> list:
    new_list.reverse()
    return new_list


print(reverse_list_basic(new_list=[1, 2, 3]))


def reverse_list_advanced(new_list: list) -> list:
    return list(reversed(new_list))


print(reverse_list_advanced(new_list=[1, 2, 3]))


# 5. Найди индекс первого вхождения заданного элемента.
def find_index_basic(new_list: list, element: int) -> int:
    for i, num in enumerate(new_list):
        if element == num:
            return i
    return -1


print(find_index_basic(new_list=[1, 2, 3], element=3))


def find_index_advanced(new_list: list, element) -> int:
    return new_list.index(element)

def find_index_advanced1(new_list: list, element: int) -> int:
    return next((i for i, num in enumerate(new_list) if num == element), -1)

print(find_index_advanced(new_list=[1, 2, 3], element=1))
