import numpy as np
import pandas as pd


def NumpyTasks():
    """
    Задача 1
    Создайте целочисленный массив Numpy. Для этого выполните следующие шаги:

    Создайте список из целых значений (не меньше 5 шт.)
    Используя метод numpy.array() переведите список в массив Numpy
    """

    import random

    regular_list = [random.randint(0, 100) for x in range(10)]
    numpy_array = np.array(regular_list)

    """
    Задача 2
    Используя индексы, выведите первый и третий элемент массива
    """

    print(numpy_array[0])
    print(numpy_array[2])

    """
    Задача 3
    Используя метод type(), проверьте тип созданного массива.
    """

    print(type(numpy_array))

    """
    Задача 4
    Используя метод sum(), найдите сумму всех элементов массива.
    """

    sum = numpy_array.sum()
    print(sum)

    """
    Задача 5
    Используя метод arange(), создайте новый массив из значений от 0 до 10.
    """

    arange_array = np.arange(start=0, stop=11)
    print(arange_array)


def PandasTasks():
    """
    Задание 1
    Воссоздайте таблицу в виде Pandas DataFrame.
    """

    """
    Длинный способ
    """

    arr = []
    for i in range(0, 4):
        subarr = []
        for j in range(0, 7):
            subarr.append(i*j)
        arr.append(subarr)

    """
    Короткий метод с использованием list comprehension
    """
    arr = [[x*j for x in range(7)] for j in range(4)]

    df = pd.DataFrame(arr)

    """
    Задание 2
    Сложите все значения в таблице по столбцам без использования циклов и условий.
    """

    sum = df.sum()
    print(sum)

    """
    Задание 3
    При помощи метода Pandas выведите размерность матрицы. Убедитесь в корректности результата.
    """

    # Если знаешь Assert, можно использовать
    # assert df.shape == (4,7)
    print(df.shape)

    """
    Задание 4
    При помощи метода Pandas выведите Series, содержащий данные из второго и пятого столбцов.
    """

    print(df[[1, 4]])

    """
    Задание 5
    Добавьте в таблицу столбец 7, содержащий значения 0, 7, 14, 21.
    """

    df[7] = [0, 7, 14, 21]

    # Опять же, если знаком с Assert :)
    # assert len(df.columns) == 8


PandasTasks()
