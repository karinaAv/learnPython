import random
def generate_list_with_random_values(list_length: int):
    return [random.randint(0, 100) for _ in range(list_length)]

print("1. Создай кортеж из 5 элементов и выведи его длину.")
def get_tuple_and_len():
    tup = tuple(generate_list_with_random_values(5))
    return tup, len(tup)

print(f'Result: {get_tuple_and_len()}')

print("2. Преобразуй список в кортеж и наоборот.")
def convert_tuple_and_list():
    cust_tup = tuple(generate_list_with_random_values(5))
    return cust_tup, list(cust_tup)

print(f'Result: {convert_tuple_and_list()}')

print("3. Найди максимальное и минимальное значение в кортеже.")
def get_max_min_in_tuple():
    cust_tup = tuple(generate_list_with_random_values(5))
    print(cust_tup)
    return max(cust_tup), min(cust_tup)

print(f'Result: {get_max_min_in_tuple()}')

print("4. Выведи первый и последний элемент кортежа.")
def get_first_last_elem_in_tuple():
    cust_tup = tuple(generate_list_with_random_values(5))
    print(cust_tup)
    return cust_tup[0], cust_tup[-1]

print(f'Result: {get_first_last_elem_in_tuple()}')

print("5. Проверь, содержится ли элемент в кортеже.")
def check_elem_in_tuple(elem, cust_tup):
    return elem in cust_tup

tup = tuple(generate_list_with_random_values(5))
print(tup)
n = int(input('Enter N: '))
print(f'Result: {check_elem_in_tuple(n, tup)}')
