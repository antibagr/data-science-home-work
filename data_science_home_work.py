"""
Задача 1
Создайте целочисленный массив Numpy. Для этого выполните следующие шаги:

Создайте список из целых значений (не меньше 5 шт.)
Используя метод numpy.array() переведите список в массив Numpy
"""

import numpy as np
import random

regular_list = [random.randint(0, 100) for x in range(10)]
numpy_array = np.array(regular_list)
numpy_array

"""
Задача 2
Используя индексы, выведите первый и третий элемент массива
"""

numpy_array[[0,2]]

"""
Задача 3
Используя метод type(), проверьте тип созданного массива.
"""

type(numpy_array)

"""
Задача 4
Используя метод sum(), найдите сумму всех элементов массива.
"""

numpy_array.sum()

"""
Задача 5
Используя метод arange(), создайте новый массив из значений от 0 до 10.
"""

arange_array = np.arange(start=0, stop=11)
arange_array


"""
Задание 1
Воссоздайте таблицу в виде Pandas DataFrame.
"""
import pandas as pd
arr = [[x*j for x in range(7)] for j in range(4)]

df = pd.DataFrame(arr)
df

"""
Задание 2
Сложите все значения в таблице по столбцам без использования циклов и условий.
"""

df.sum()

"""
Задание 3
При помощи метода Pandas выведите размерность матрицы. Убедитесь в корректности результата.
"""

df.shape

"""
Задание 4
При помощи метода Pandas выведите Series, содержащий данные из второго и пятого столбцов.
"""

df[[1, 4]]

"""
Задание 5
Добавьте в таблицу столбец 7, содержащий значения 0, 7, 14, 21.
"""

df[7] = [0, 7, 14, 21]
df
