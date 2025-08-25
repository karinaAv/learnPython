Конечно! Вот список **вопросов** в формате Markdown, чтобы можно было удобно копировать:

````
## Список вопросов

1. Что выведет этот код и почему?  
   ```python
   a = 5
   b = "5"
   print(a + b)
````

2. Какой будет тип у переменной `x` после выполнения?

   ```python
   x = 3.0
   x = int(x)
   ```
3. Верно ли, что переменная в Python хранит сам объект (например число), а не ссылку на него? Объясни.
4. Что получится в результате выполнения?

   ```python
   my_list = [1, 2, 3]
   my_list.append([4, 5])
   print(my_list)
   ```
5. Чем отличаются методы `.append()` и `.extend()` у списка?
6. Как срезать список так, чтобы взять каждый второй элемент? Например, из `[10, 20, 30, 40, 50]` получить `[10, 30, 50]`.
7. Что выведет этот код?

   ```python
   a = [1, 2, 3]
   b = a
   b.append(4)
   print(a)
   ```
8. Что будет результатом этого выражения?

   ```python
   x = "123"
   y = [int(i) for i in x]
   print(y)
   ```
9. Что выведет этот код?

   ```python
   lst = [1, 2, 3, 4, 5]
   print(lst[-3:-1])
   ```
10. Что выведет этот код и почему?

    ```python
    a = [1, 2, 3]
    a = a * 2
    print(a)
    ```
11. Что выведет этот код?

    ```python
    a = [0, 1, 2, 3, 4]
    a[1:4] = [9, 8]
    print(a)
    ```
12. Что выведет этот код?

    ```python
    lst = [0, 1, 2, 3, 4, 5]
    lst[::2] = [10, 20, 30]
    print(lst)
    ```
13. Что выведет этот код и почему?

    ```python
    a = [1, 2, 3]
    b = a * 2
    b[0] = 10
    print(a)
    print(b)
    ```
14. Что выведет этот код и почему?

    ```python
    a = [[1, 2], [3, 4]]
    b = a[:]
    b[0][0] = 10
    print(a)
    print(b)
    ```
15. Что выведет этот код?

    ```python
    import copy
    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)
    b[0][0] = 10
    print(a)
    print(b)
    ```
16. Что выведет этот код?

    ```python
    lst = [1, 2, 3, 4, 5, 6, 7]
    print(lst[1:-1:2])
    ```
17. Что выведет этот код?

    ```python
    lst = [10, 20, 30, 40, 50]
    print(lst[-2::-2])
    ```
18. Что выведет этот код и почему?

    ```python
    x = 5
    y = x
    y += 3
    print(x, y)
    ```
19. Что выведет этот код?

    ```python
    lst = [1, 2, 3, 4, 5]
    lst[::3] = [10, 20]
    print(lst)
    ```
20. Что выведет этот код и почему?

    ```python
    x = "5"
    b = 2
    c = x * b
    print(c)
    ```
21. Что выведет этот код?

    ```python
    lst = [1, "2", 3]
    total = 0
    for x in lst:
        total += int(x)
    print(total)
    ```
22. Что выведет этот код?

    ```python
    x = 7
    y = float(x)
    z = str(y)
    print(type(x), type(y), type(z))
    ```
23. Что выведет этот код?

    ```python
    lst = [3, 1, 4, 1, 5]
    lst.sort()
    print(lst)
    lst.reverse()
    print(lst)
    ```
24. Что выведет этот код?

    ```python
    lst = [1, 2]
    lst.append([3, 4])
    lst.extend([5, 6])
    print(lst)
    ```
25. Что выведет этот код?

    ```python
    lst = [0, 1, 2, 3, 4, 5, 6]
    print(lst[1:-1:2])
    ```
26. Что выведет этот код?

    ```python
    x = "3.5"
    y = float(x) + 2
    z = int(y)
    print(z)
    ```
27. Что выведет этот код?

    ```python
    lst = [1, 2, 3, 4, 5]
    print(lst[:: -1][1])
    ```
28. Что выведет этот код?

    ```python
    a = [1, 2, 3]
    b = a
    b += [4, 5]
    print(a)
    print(b)
    ```
29. Что выведет этот код?

    ```python
    a = [[1, 2], [3, 4]]
    b = a[:]
    b[1] = [5, 6]
    print(a)
    print(b)
    ```
30. Что выведет этот код?

    ```python
    x = 3
    y = x
    x = x + 2
    print(x, y)
    ```
31. Что выведет этот код?

    ```python
    lst = [1, 2]
    lst.append(3)
    lst.extend([4, 5])
    print(lst)
    ```
32. Что выведет этот код?

    ```python
    lst = [0, 1, 2, 3, 4, 5, 6]
    print(lst[5:0:-2])
    ```
33. Что выведет этот код?

    ```python
    a = [[1, 2], [3, 4]]
    b = a
    b[0][1] = 10
    print(a)
    print(b)
    ```
34. Что выведет этот код?

    ```python
    x = "7"
    y = int(x) + 3.5
    z = str(y)
    print(type(x), type(y), type(z))
    ```
35. Что выведет этот код?

    ```python
    lst = [1, 2, 3, 4, 5]
    x = lst.pop(2)
    print(x, lst)
    ```
36. Что выведет этот код?

    ```python
    lst = [1, 2, 3]
    lst.insert(1, 10)
    print(lst)
    ```
37. Что выведет этот код?

    ```python
    lst = [0, 1, 2, 3, 4, 5, 6]
    lst[1:6:2] = [10, 20, 30]
    print(lst)
    ```
38. Что выведет этот код?

    ```python
    a = 5
    b = 2
    c = a / b
    d = a // b
    print(c, d)
    ```
39. Что выведет этот код?

    ```python
    lst = [1, 2, 3, 4]
    x = lst.pop()
    print(x, lst)
    ```
40. Что выведет этот код?

    ```python
    lst = [1, 2]
    lst *= 2
    lst.extend([5, 6])
    print(lst)
    ```
41. Что выведет этот код?

    ```python
    x = [1, 2]
    y = x
    y += [3, 4]
    print(x, y)
    ```
42. Что выведет этот код?

    ```python
    lst = ["1", "2", "3"]
    total = sum(int(x) for x in lst)
    print(total)
    ```
