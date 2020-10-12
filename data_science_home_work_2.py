# Ultra light
# Задача 1

# Напишите функцию, которая будет выводить количество букв в слове.
# Проверьте при помощи этой функции, сколько букв в слове восьмидесятивосьмимиллиметровое.

def count_letters_in_a_word(word: str) -> int:
    return len(word)

count_letters_in_a_word('восьмидесятивосьмимиллиметровое')

# Задача 2
#
# Напишите функцию, которая выводит таблицу умножения (от 1 до 9) для указанного числа в следующем формате:
#
# 1 * 3 = 3
#
# 2 * 3 = 6
#
# 3 * 3 = 9
#
# ...
#
# 9 * 3 = 27


def multiplication_table_for_a_number(number: int) -> None:

    for multiplier in range(1, 10):
        print(f"{multiplier} * {number} = {multiplier*number}")

multiplication_table_for_a_number(3)

# Задача 3
#
# Напишите функцию, которая выводит сумму, разность и произведение двух, поданных на вход чисел.


def math_operations(a: int, b: int) -> None:
    print(a+b)
    print(a-b)
    print(a*b)

math_operations(15, 10)


# Задача 4
#
# Импортируйте функцию sin из модуля math с присвоением ей псевдонима sinus.
# Посчитайте при помощи импортированной функции, чему будет равен синус единицы

from math import sin as sinus

result = sinus(1)
print(result)

# Задача 5
#
# Напишите лямбда-функцию, которая считает куб числа.

cube = lambda x: x**3
assert cube(3) == 27

# Задача 1
# Загрузите таблицу city_temperature.csv в pandas DataFrame. При помощи встроенных методов библиотеки Pandas найдите количество стран, среднее значение температуры в которых бывает больше 100 градусов по Фаренгейту.
#
# Циклы и условия использовать нельзя.
#
# Описание базы:
# Region - регион
#
# Country - страна
#
# State - штат (если есть)
#
# Month - месяц
#
# Day - день
#
# Year - год
#
# AvgTemperature - средняя температура в Фаренгейтах
#
# Ссылка на базу: https://drive.google.com/file/d/1bLiz_81Kb4pMryEalRe66jS38_F6vwMX/view?usp=sharing

!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

import pandas as pd

file_name = 'city_temperature.csv'

def DownloadCSV() -> None:
    # Автор кода
    # https://medium.com/@krashnagurme
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)
    downloaded = drive.CreateFile({'id':'1bLiz_81Kb4pMryEalRe66jS38_F6vwMX'})
    downloaded.GetContentFile(file_name)

import os

if not os.path.exists(file_name):
  DownloadCSV()

df = pd.read_csv(file_name, low_memory=True)

all_countries = df['Country'].nunique()

countries_filtered_by_average_temperature = df[df['AvgTemperature'] > 100]['Country'].nunique()
print("all countries", all_countries)
print("Countries where average temperature is higher than 100 degrees", countries_filtered_by_average_temperature)

# Задача 2
# Найдите медиану столбца AvgTemperature при помощи встроенных методов библиотеки Pandas.

df['AvgTemperature'].mean()

# Задача 3
# Найдите число записей в базе данных для первого января 1995 года или первого января 2018 года при помощи масок.

df[((df['Year'] == 1995) | (df['Year'] == 2018)) & (df['Month'] == 1) & (df['Day'] == 1)].size

# Задание 4
# Получите список всех уникальных значений стран в таблице при помощи встроенных методов.

# Я НЕ ПОНЯЛ формулировки задания. Если он хочет уникальный список стран, то
pd.unique(df['Country'].values.ravel('K'))
# Если он хочет уникальный список значений средней температуры, то
pd.unique(df['AvgTemperature'].values.ravel('K'))
# Если же нужно найти уникальные значение для обеих стобцов, то
pd.unique(df[['AvgTemperature', 'Country']].values.ravel('K'))


# Задача 5
# При помощи переводчика или при помощи своих знаний переведите названия столбцов на русский язык.
# Замените в таблице английские названия столбцов на русские

!pip install googletrans

import googletrans
from googletrans import Translator
translator = Translator()

df_ru = df.copy()
df_ru.rename(columns=lambda x: translator.translate(x, src='en', dest='ru').text if x != "State" else "Штат", inplace=True)
df_ru.head()


# **Задача 1**
# "На основе данных x и y, представленных ниже, постройте 2 графика plot и scatter на разных плоскостях."
import matplotlib.pyplot as plt

x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]

fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].scatter(x, y)
plt.show()

# **Задача 2**
# Добавьте на предыдущий график plot линии сетки, подписи осей х и y, название графика \"Самолет\". Сделайте размер графика (6, 3)

plt.rcParams["figure.figsize"] = (6,3)
fig.suptitle('Самолёт и его точки')
plt.rc('grid', linestyle="-", color='black')
plt.plot(x, y)
plt.grid(True)
plt.show()

# **Задача 3**
# Постройте, на основе приведенного ниже словаря, диаграмму. Ключи словаря будут подписями на оси х.
# Данные для построения диаграммы

data = {'Яблоки': 10, 'Апельсины': 15, 'Лимоны': 5, 'Лайм': 20}
names = list(data.keys())
values = list(data.values())

plt.bar(names, height=values)
plt.show()

# **Задача 4**
# Постройте boxplot на основе списка spis, приведенного ниже. Измените цвет графика на зеленый.

spis = [2, 4, 1, 5, 6, 13]

box = plt.boxplot(spis, patch_artist=True)
box['boxes'][0].set_facecolor('green')
# plt.setp(plot, color='green')
plt.show()

# **Задача 5**
# Постройте график lmplot на основе датафрейма, приведенного ниже (строить нужно по данным столбца 'x' и 'y')

# Подгружаем датасет "anscombe"
df = sns.load_dataset("anscombe")

# Выводим первые 5 строк датасета
# df.head(5)
sns.lmplot(x='x', y='y', data=df)
plt.show()
