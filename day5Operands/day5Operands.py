print("""Задача 1 — Проверка диапазона
Напиши код, который проверяет, входит ли число x = 15 в диапазон от 10 до 20 включительно, и выводит True или False.
Используй оператор and.""")
def check_range(num):
    return 10 <= num <= 20

n = int(input('Enter  N: '))
print(check_range(n))

print("""Задача 2 — Проверка чётности или кратности
Пусть есть число n = 12.
Нужно проверить: является ли число чётным или кратным 5. Используй or."""
)
def check_even_or_multiple(num):
    return num % 2 == 0 or num % 5 == 0

n = int(input('Enter  N: '))
print(check_even_or_multiple(n))

print("""Задача 3 — Отрицание условия
Пусть user_active = False.
Выведи True, если пользователь не активен. Используй not.""")
def check_user_inactive(user_active):
    return not user_active

print(check_user_inactive(user_active=True))
print(check_user_inactive(user_active=False))

print("""Задача 4 — Побитовое И и ИЛИ
Даны числа a = 6 и b = 3.
Найди и выведи результат:
a & b (побитовое И)
a | b (побитовое ИЛИ)""")
def get_bitwise(num_a, num_b):
    return num_a & num_b, num_a | num_b

print(f'Result: {get_bitwise(6, 3)}')

print("""Задача 5 — Побитовое исключающее ИЛИ
Есть числа x = 10 и y = 12.
Вычисли x ^ y и объясни, в чём отличие этого оператора от обычного or.""")
def get_xor_elements(x, y):
    return x ^ y

print(f'Result: {get_xor_elements(10, 12)}')

print("""Задача 6 — Общие элементы списков (побитовое И)
Даны два списка:
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
Найди элементы, которые встречаются и в a, и в b, используя &.
Подсказка: преобразуй списки в множества.
Ожидаемый результат:
{3, 4, 5}""")
import random
def generate_list_with_random_values(list_length: int):
    return [random.randint(0, 100) for _ in range(list_length)]

def get_common_elements(list_a, list_b):
    print(list_a)
    print(list_b)
    return set(list_a) & set(list_b)

print(f'Result: {get_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])}')

print("""Задача 7 — Все уникальные элементы из двух списков (побитовое ИЛИ)
Есть два списка:
x = [10, 20, 30]
y = [30, 40, 50]
Найди множество, содержащее все уникальные элементы из x и y, используя |.
Ожидаемый результат:
{10, 20, 30, 40, 50}""")
def get_unique_elements(list_a, list_b):
    print(list_a)
    print(list_b)
    return set(list_a) | set(list_b)

print(f'Result: {get_unique_elements(generate_list_with_random_values(5), generate_list_with_random_values(5))}')

print("""Задача 8 — Симметрическая разность (побитовое XOR)
Даны списки:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
Найди элементы, которые встречаются только в одном списке (не общие). Используй оператор ^.
Подсказка: преобразуй списки в множества перед применением ^.
Ожидаемый результат:
{1, 2, 5, 6}""")
def get_symmetric_difference(list_a, list_b):
    print(list_a)
    print(list_b)
    return set(list_a) | set(list_b)

print(f'Result: {get_symmetric_difference(generate_list_with_random_values(5), generate_list_with_random_values(5))}')
