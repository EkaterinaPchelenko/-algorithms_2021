"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list)-n):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        n += 1
    return my_list


def red_bubble_sort(my_list):
    n = 1
    c = 0  # Переменная, которая считает кол-во не совершённых сортировок за проход по списку
    while n < len(my_list):
        for i in range(len(my_list)-n):
            if my_list[i] < my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            else:
                c += 1
        if c == len(my_list)-n:
            return my_list
        n += 1
    return my_list


nums_list = [randint(-100, 100) for i in range(10)]
special_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]
print(nums_list)
print(bubble_sort(nums_list[:]))

print(timeit("bubble_sort(nums_list[:])", globals=globals()))
# Время выполнения: 7.2937324
print(timeit("red_bubble_sort(nums_list[:])", globals=globals()))
# Время выполнения: 8.1105216
# Попробуем передать функции уже отсортированный массив
print(timeit("red_bubble_sort(special_list[:])", globals=globals()))
# Время выполнения: 1.2424230999999981
# Как мы видим, улутшения для уже отсортированного массива работают.
# Но в случае массива, созданного случайной генерацией чисел, это улучшение практически бесполезно,
# так как вероятность того, что мы сгенерируем отсортированный массив, катастрофически мала.