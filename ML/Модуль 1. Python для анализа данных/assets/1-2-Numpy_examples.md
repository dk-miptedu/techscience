---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region id="hlvJntDusO6C" -->
## Использование NumPy в задачах обработки данных
<!-- #endregion -->

<!-- #region id="v0sqNPBytaeA" -->
Перед использованием настоящего ноутбука, пожалуйста, проверьте актуальность ссылок на датасеты и изображения для реализации примеров. Используемые датасеты и изображения, вы найдете в дополнительных материалах.
<!-- #endregion -->

<!-- #region id="PQodLdD3kH7u" -->
## Генерация мелодии
<!-- #endregion -->

<!-- #region id="jWiUhfnLtE0j" -->
Задача заключается в генерации мелодии по заранее заданным нотам. Ноты соответствуют гамме до мажор частот первой октавы. Звучание нот реализуем по таблице частот.
<!-- #endregion -->

<!-- #region id="Wou3ZJFQv2u-" -->
Импортируем библиотеку `NumPy` и библиотеку для озвучки аудио. Создадим звуковой ряд из частот первой октавы, частоту дискретизации и длительность звучания отдельной ноты.

**Частота дискретизации** — количество значений сигнала, записываемых в секунду.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="oQmhZ27bL_dk" outputId="4363c4e8-7fec-43f7-8398-ddf7e3bc1d02" executionInfo={"status": "ok", "timestamp": 1688564687901, "user_tz": -180, "elapsed": 14, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import numpy as np
# библиотека для озвучки аудио
from IPython.display import Audio

#частота дискретизации (Гц)
samplerate = 44100

time = 1.0

# частоты нот (Гц) первой октавы: до, ре, ми, фа, соль, ля, си
frequency = np.array([261.63, 293.66, 329.63, 349.23, 392, 440, 493])

N_notes = frequency.size
N_notes
```

<!-- #region id="IdL1jZ7EwAQG" -->
Код реализует создание звуков длительностью 1 секунда по частотам , заданным в `NumPy`. После чего полученные звуки складываются и получается единый звукоряд из 7 нот.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 75} id="Db9mgAX0QlHf" outputId="ccdc965b-4a34-4868-83d1-885f902440a4" executionInfo={"status": "ok", "timestamp": 1688564692762, "user_tz": -180, "elapsed": 22, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
wave_sum = np.array([])

# мелодия с одинаковыми длительностями

for i in range(0,N_notes):
  # Генерация значений между 0 и 1 секундой
    samples = np.arange(44100 * time) / 44100.0
  # Синусоидальная функция частоты сигнала w(t) = A*sin(2*pi*f*t)
    wave = 10000 * np.sin(2 * np.pi * frequency[i] * samples)
  # конвертация в  wav формат (16 бит) и складывание сигналов
    wave_wave = np.array(wave, dtype=np.int16)
    wave_sum = np.append(wave_sum, wave_wave)

Audio(wave_sum, rate=samplerate)
```

<!-- #region id="ixiQ3Mrcvelo" -->
**Спектрограмма** — графическое представление спектра сигнала в зависимости от времени.

Спектрограмма может быть полезной для анализа звуковых сигналов, таких как речь, музыка или звуки окружающей среды. Также может помочь выявить особенности изменения сигнала технических систем от времени.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 455} id="cndCfpU9uX3H" outputId="299c23d3-1566-47d6-b66a-3505f7766b43" executionInfo={"status": "ok", "timestamp": 1688462549086, "user_tz": -180, "elapsed": 892, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
# Построение спектрограммы

# NFFT - количество точек для вычисления быстрого преобразования Фурье при вычислении спектрограммы
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.specgram(wave_sum,Fs = samplerate, NFFT = 2048)
plt.ylim([0, 1000])
plt.xlabel('Время, сек')
plt.ylabel('Частота, Гц')
plt.show()
```

<!-- #region id="PzoEKKmM4vz7" -->
**Вывод:** `NumPy` позволяет работать с аудио данными и визуализировать важные характеристики звука. В том числе отображать изменение основного тона с помощью спектрограммы
<!-- #endregion -->

<!-- #region id="_xJ492vtZZxY" -->
## Работа с табличными данными и векторами
<!-- #endregion -->

<!-- #region id="kNtdtQ4dzq4k" -->
В этом примере мы будем работать с данными о температурах городов России.

Загрузим данные из файла `'temperature_russian_cities.csv'`.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 626} id="lkYwXES-EsYe" executionInfo={"status": "ok", "timestamp": 1688462750511, "user_tz": -180, "elapsed": 334, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="c143610b-607f-4d09-eb68-2f5062f74a88"
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/andreizouk/ML/main/temperature_russian_cities.csv")
data
```

<!-- #region id="ISoK9aUy8jn4" -->
Переведем данные столбца `'The temperature of the warmest month, °C'` в числовые.
<!-- #endregion -->

```python id="h0R-nHVOLcDD"
temperatures = pd.to_numeric(data['The temperature of the warmest month, °C'])
```

<!-- #region id="tTe120NMMLU_" -->
Конвертируем формат `Pandas` в `NumPy`.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="5tWLJc1k8mpw" executionInfo={"status": "ok", "timestamp": 1688462795761, "user_tz": -180, "elapsed": 346, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="d1c843d5-e198-4284-fff7-62f7fb0ad318"
temperatures_numpy=temperatures.to_numpy()
temperatures_numpy
```

<!-- #region id="ilBC1Jww86JA" -->
Вычислим среднее значение средней температуры городов в самый теплый месяц.
<!-- #endregion -->

```python id="6ntnGDJ14pk4" colab={"base_uri": "https://localhost:8080/"} outputId="8b6d76d5-9bde-4969-d67f-e1e6ad919ac4" executionInfo={"status": "ok", "timestamp": 1688462804820, "user_tz": -180, "elapsed": 329, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
# средняя температура городов в самый теплый месяц
np.mean(temperatures_numpy)
```

<!-- #region id="c-Xfcg084qKf" -->
***Нормализация переменных***

**Нормализация** — это изменение масштаба данных из исходного диапазона, чтобы все значения находились в диапазоне от 0 до 1.

Нормализация может быть полезной в некоторых алгоритмах машинного обучения, когда данные временных рядов имеют входные значения с различными масштабами. Это может потребоваться для алгоритмов, таких как k-Nearest соседей, которые используют вычисления расстояний,линейную регрессию и искусственные нейронные сети.


<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="oBoq36-RGrsw" outputId="7257268d-b3f7-45eb-8c1d-5808c722743d" executionInfo={"status": "ok", "timestamp": 1688462859540, "user_tz": -180, "elapsed": 457, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
# нормализация данных
print((temperatures_numpy- np.min(temperatures_numpy)) / (np.max(temperatures_numpy) - np.min(temperatures_numpy)))
```

<!-- #region id="dKajTl5kK_sb" -->
**Стандартизация переменных**

Стандартизация набора данных включает в себя изменение масштаба распределения значений так, чтобы среднее значение наблюдаемых значений было 0, а стандартное отклонение - 1.

Это можно рассматривать как вычитание среднего значения или центрирование данных.

Как и нормализация, стандартизация может быть полезной  в некоторых алгоритмах машинного обучения, таких как машины опорных векторов, линейная и логистическая регрессия

Стандартизация предполагает, что ваши наблюдения соответствуют гауссовскому распределению со средним значением и стандартным отклонением.




<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="R3oJUxT0LJNL" outputId="ae2e1c9e-ae50-42b8-8506-1f186fbad443" executionInfo={"status": "ok", "timestamp": 1688462856120, "user_tz": -180, "elapsed": 325, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
print((temperatures_numpy- np.min(temperatures_numpy)) / (np.std(temperatures_numpy)))
```

<!-- #region id="FQLfR97adI1i" -->
**Операции с векторами**

*   `np.linalg.norm(x)` — поиск нормы векторов;

*   `np.linalg.norm(x-y)` — расстояние между векторами;

*   `np.dot()` — скалярное произведение двух векторов;

*   `np.linalg.solve()` — решения системы линейных уравнений;

*   `np.linalg.lstsq()` — метод наименьших квадратов.
<!-- #endregion -->

<!-- #region id="AsDnk-949yg8" -->
Выделим широту и долготу городов из таблицы и переведем ее в числовой вид:
<!-- #endregion -->

```python id="xe_9yc717DKc"
# широта городов
Latitude = pd.to_numeric(data['Latitude']).to_numpy()

# долгота городов
Longitude = pd.to_numeric(data['Longitude']).to_numpy()
```

<!-- #region id="XbgNDhrN7jKK" -->
Рассчитаем прямое расстояние между Новосибирском и остальными городами:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 214} id="M6H80qAa7pUy" outputId="9a9183df-2547-4569-95bd-a05df06d9066" executionInfo={"status": "ok", "timestamp": 1688462910516, "user_tz": -180, "elapsed": 418, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data[data['City']=='Новосибирск']
```

<!-- #region id="GNEw2kMZ9h-k" -->
Из данных видим:
*   широта Новосибирска  55.008353 град
*   долгота Новосибирска 82.935733 град
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="lC4x6DGZ_Onb" outputId="f8c1d3bf-be79-4617-a094-8002494969b8" executionInfo={"status": "ok", "timestamp": 1688462942114, "user_tz": -180, "elapsed": 334, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import math

R = 6373.0 # Расстояние до центра Земли

#Координаты Новосибирска переведенные в радианы
lat1 = 55.008353*np.pi/180
lon1 = 82.935733*np.pi/180

lon2 = Longitude*np.pi/180
lat2 = Latitude*np.pi/180

dlon = lon2 - lon1
dlat = lat2 - lat1

a = (np.sin(dlat/2))**2 + np.cos(lat1) * np.cos(lat2) * (np.sin(dlon/2))**2
c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
distance_Novosibirsk = R * c
#расстояние от Новосибирска до городов России
distance_Novosibirsk


```

<!-- #region id="oYblgW58OYMV" -->
Посчитаем максимальное расстояние:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="ZqjImcWeOc0O" executionInfo={"status": "ok", "timestamp": 1688462949481, "user_tz": -180, "elapsed": 306, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="f3300d3e-9e3a-488f-9f1f-59f4cfb9d899"
np.max(distance_Novosibirsk)
```

<!-- #region id="Z21-4BuSBWYo" -->
Для сравнения вычислим максимальное геодезическое расстояние — расстояние, измеренное вдоль поверхности Земли с помощью специальной библиотеки, учитывающей несферичность земли. Для этого подгрузим библиотеку `geopy.distance`.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="8g0ROUt7Bnp7" outputId="b38943e2-f9bc-49ea-8bf1-67d993287580" executionInfo={"status": "ok", "timestamp": 1688462963838, "user_tz": -180, "elapsed": 9, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import geopy.distance

coords_1 = (lat1*180/np.pi, lon1*180/np.pi)
coords_2 = (lat2, lon2)

max_dist = 0
for i in range(1,len(lat2)):
    geodesic_distance = geopy.distance.geodesic(coords_1, (lat2[i]*180/np.pi,lon2[i]*180/np.pi)).km
    if geodesic_distance > max_dist:
      max_dist = geodesic_distance
max_dist
```

<!-- #region id="1dtcMCEbGOOK" -->
Рассчитаем расстояния до всех городов от Москвы:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 214} id="O6qxhzQ9GYHb" outputId="681d7774-41fa-432c-d084-8eee2c1a2e6e" executionInfo={"status": "ok", "timestamp": 1688462972647, "user_tz": -180, "elapsed": 313, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data[data['City']=='Москва']
```

<!-- #region id="DJjja-UuGyTT" -->
Географические координаты Москвы:
*   широта Москвы 55.755826 град
*   долгота Москвы 37.6173 град
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="3GOY6D5FGHg_" outputId="dfe30aea-85cb-4108-9f24-618be1308765" executionInfo={"status": "ok", "timestamp": 1688462982122, "user_tz": -180, "elapsed": 333, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import math

R = 6373.0 # Расстояние до центра Земли

# Координаты Москвы
lat1 = 55.755826*np.pi/180
lon1 = 37.6173*np.pi/180

lon2 = Longitude*np.pi/180
lat2 = Latitude*np.pi/180

dlon = lon2 - lon1
dlat = lat2 - lat1

a = (np.sin(dlat/2))**2 + np.cos(lat1) * np.cos(lat2) * (np.sin(dlon/2))**2
c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
distance_Moscow = R * c

#расстояние от Москвы до городов России

distance_Moscow

```

<!-- #region id="DtUhIZlTOQjw" -->
Посчитаем максимальное расстояние:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="qEYWtJ_EOUrt" executionInfo={"status": "ok", "timestamp": 1688462988116, "user_tz": -180, "elapsed": 388, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="6a9505ab-a201-45aa-dd05-d68479472c69"
np.max(distance_Moscow)
```

<!-- #region id="zc6GtwE8HoP8" -->
Посчитаем норму для расстояний от Новосибирска.
Корень квадратный из сумм квадратов — евклидово расстояние многомерного пространства.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="mIGBdhKaH6zq" outputId="781ca4ca-bc85-47f6-f931-4e2e5b03ed1e" executionInfo={"status": "ok", "timestamp": 1688463008361, "user_tz": -180, "elapsed": 449, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
#Норма расстояний для Новосибирска

np.linalg.norm(distance_Novosibirsk)
```

<!-- #region id="3kWUNZPEGSG-" -->
Норма для расстояний от Москвы:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="AFfTBxBUIPFr" outputId="7e4a0dce-7f55-44ae-f52c-b638ed2216ae" executionInfo={"status": "ok", "timestamp": 1688463016433, "user_tz": -180, "elapsed": 307, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
#Норма расстояний для Москвы

np.linalg.norm(distance_Moscow)
```

<!-- #region id="XkL4Y4n5GYCs" -->
Норма расстояний между векторами вычисленных расстояний Новосибирска и Москвы:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="lvxkKsNOIxaT" outputId="8883be71-e41c-4fc4-bee2-47f4d71a3db1" executionInfo={"status": "ok", "timestamp": 1688463034082, "user_tz": -180, "elapsed": 306, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
#Норма разницы векторов Москвы и Новосибирска
np.linalg.norm(distance_Moscow - distance_Novosibirsk)

```

```python colab={"base_uri": "https://localhost:8080/"} id="p2okP9QiI8yK" outputId="718e36bd-7404-46c9-b266-1998be2fda67" executionInfo={"status": "ok", "timestamp": 1688463036431, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
#Норма разницы векторов Новосибирска и Москвы
np.linalg.norm(distance_Novosibirsk- distance_Moscow)
```

<!-- #region id="psJSwg_cbHNk" -->
**Метод наименьших квадратов**

**Задача:** Подобрать уравнение прямой  `y = mx + c`, наиболее близкой к экспериментальным данным.

В качестве экспериментальных данных возьмем широту города и его температуру в самый теплый месяц.

И посмотрим, можно ли построить уравнение прямой, аппроксимирующее эту зависимость.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 423} id="GHUeQ4eqKaC6" outputId="b47e59b6-4835-4c8a-ba4f-20ae41ddfd48" executionInfo={"status": "ok", "timestamp": 1688463071823, "user_tz": -180, "elapsed": 384, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data[['Latitude','The temperature of the warmest month, °C']]
```

```python id="Eyj-QsEaMdfL"
latitude_warm = pd.to_numeric(data['Latitude']).to_numpy()
temperatures_warm = pd.to_numeric(data['The temperature of the warmest month, °C']).to_numpy()
```

```python id="IegeH_WZbK0B"
x = latitude_warm
y = temperatures_warm
```

<!-- #region id="9VTRV1N4cSwR" -->
Мы можем переписать линейное уравнение как `y = Ap`, где `A = [[x 1]]` и `p = [[m], [c]]`.

Теперь используем `lstsq` для оценки `p`:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="pg4jHhrGcHZy" outputId="73c6fa99-4552-438b-b538-bc59718b7cb4" executionInfo={"status": "ok", "timestamp": 1688463099258, "user_tz": -180, "elapsed": 317, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
A = np.vstack([x, np.ones(len(x))]).T
A
```

```python colab={"base_uri": "https://localhost:8080/"} id="kPoJrA-pcdhC" outputId="85e93dad-b7a0-4159-c8c7-229bb3f02628" executionInfo={"status": "ok", "timestamp": 1688463114280, "user_tz": -180, "elapsed": 347, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
m, c
```

<!-- #region id="VKwzXZG5MM7b" -->
Теперь покажем на графике насколько данные таблицы близки к полученной прямой с учетом вычисленных коэффициентов.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 430} id="LTCloaaBclGy" outputId="1d8ee5f4-e40a-4615-a996-e5ae61490ed3" executionInfo={"status": "ok", "timestamp": 1688463138994, "user_tz": -180, "elapsed": 367, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import matplotlib.pyplot as plt
_ = plt.plot(x, y, 'o', label='Экспериментальные данные', markersize=10)
_ = plt.plot(x, m*x + c, 'r', label='Подобранная прямая')
_ = plt.legend()
plt.show()
```

<!-- #region id="FCU-xfXzy1TE" -->
**Выводы:**

1. Табличные данные могут быть преобразованы в формат `NumPy`, и с ними возможно проводить операции как с векторами, в том числе рассчитывать различные нормы, средние.
2. Норма может быть использована в качестве признака сравнения размещения городов и использована в машинном обучении.
3. На основании операции метода наименьших квадратов в `NumPy` может быть получена линейная аппроксимация одной характеристики относительно другой.
<!-- #endregion -->

<!-- #region id="DHHMAbUMPeDR" -->
## Работа с изображением с использованием NumPy
<!-- #endregion -->

<!-- #region id="7KGQaCNPyoFp" -->
Рассмотрим основные операции, которые можно выполнять с изображением с помощью `NumPy`. При этом изображение будет представлено в виде матриц.
<!-- #endregion -->

<!-- #region id="gQtKQyEYMWid" -->
Загрузим необходимые библиотеки , загрузим изображение для работы и переведем его в формат `numpy array`.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 597} id="7ia2fvHkckay" outputId="c7ac34e5-b780-40ff-ccba-4ada084bdbb0" executionInfo={"status": "ok", "timestamp": 1688463356271, "user_tz": -180, "elapsed": 2586, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import urllib.request

url1 = "https://raw.githubusercontent.com/andreizouk/ML/main/dog.jpg"

urllib.request.urlretrieve(url1, 'dog.jpg')

img_initial = np.array(Image.open(r"dog.jpg"))



img = np.array(img_initial)

#np.array(Image.open('../dog.jpg'))
plt.figure(figsize=(8,8))
plt.imshow(img)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 470} id="WX8AO26V2v5Z" executionInfo={"status": "ok", "timestamp": 1688463369619, "user_tz": -180, "elapsed": 3818, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="99771fbd-3165-4d5f-9014-0ddcd565aa95"
url2 = "https://raw.githubusercontent.com/andreizouk/ML/main/mountains.jpeg"


urllib.request.urlretrieve(url2, 'mountains.jpeg')

img_mountain = np.array(Image.open(r"mountains.jpeg"))

img_m = np.array(img_mountain)

plt.figure(figsize=(8,8))
plt.imshow(img_m)

```

<!-- #region id="W3cOzbZFMgxU" -->
Выведем размерности матриц, характеризующих изображение в `NumPy`.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="qvfECblAeHCF" outputId="e758df12-489b-4180-c713-3ed9c5a3fe41" executionInfo={"status": "ok", "timestamp": 1688463377045, "user_tz": -180, "elapsed": 327, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
print('# of dims: ',img.ndim)
print('img shape: ',img.shape)
print('dtype: ',img.dtype)
```

```python colab={"base_uri": "https://localhost:8080/"} id="Xmdt7vJ0eQjk" outputId="03e47b1e-ae8a-49ea-ed17-38e04dc35b60" executionInfo={"status": "ok", "timestamp": 1688463397655, "user_tz": -180, "elapsed": 314, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
# значения пикселей [R, G, B]
print(img[20, 20])

# минимальный пиксель в канале B
print(img[:, :, 2].min())
```

<!-- #region id="7sZj5n5sBEOw" -->
1. Вырезка изображения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 217} id="u6tmRAAoBHZl" outputId="e4f83442-c518-4f0e-a48a-49b841be65bf" executionInfo={"status": "ok", "timestamp": 1688463417694, "user_tz": -180, "elapsed": 419, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
image_arr = img[100:300, 100:200]

# Convert array to image
image = Image.fromarray(image_arr)

# Display image
image.show()
```

<!-- #region id="4vWYUUkFf7Zb" -->
2. Вырезание изображения по краям.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 365} id="2Tt3n7Hrf9ST" outputId="d10fd26a-2670-4b27-b722-91d43557be2f" executionInfo={"status": "ok", "timestamp": 1688463454358, "user_tz": -180, "elapsed": 2662, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

fig = plt.figure(figsize=(10, 10))

fig.add_subplot(1, 2, 1)
plt.imshow(img)
plt.title('Оригинал')

img0 = img[128:-128, 128:-128, :]

fig.add_subplot(1, 2, 2)
plt.imshow(img0)
plt.title('Обрезанное по краям')
```

<!-- #region id="rAAkvq7FgBpb" -->
3. Вставка вырезанного изображения с уменьшением размера.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 419} id="yesYMqAvgCKk" outputId="3897f573-7bb3-4827-bacb-f02cf4b65c33" executionInfo={"status": "ok", "timestamp": 1688463502124, "user_tz": -180, "elapsed": 1617, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
src = np.array(Image.open('dog.jpg').resize((128, 128)))
dst = np.array(Image.open('dog.jpg').resize((256, 256))) // 2

dst_copy = dst.copy()
dst_copy[64:128, 128:192] = src[0:64, 0:64]

fig = plt.figure(figsize=(10, 10))

fig.add_subplot(1, 2, 1)
plt.imshow(src)
plt.title('Оригинал')

fig.add_subplot(1, 2, 2)
plt.imshow(dst_copy)
plt.title('Вставлено вырезанное изображение')
```

<!-- #region id="ZOtLyu0sehfL" -->
4. Поворот изображения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 452} id="J80sNOw8e4Ed" outputId="8a32de28-59da-4f6e-93e0-b8e9bef19400" executionInfo={"status": "ok", "timestamp": 1688463531291, "user_tz": -180, "elapsed": 1109, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
# или можно использовать
img = np.array(Image.open('dog.jpg'))
plt.imshow(np.rot90(img))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 469} id="C7m8C3u-RoWX" outputId="5cdb5548-3ade-4a61-9f35-ff0e41e68175" executionInfo={"status": "ok", "timestamp": 1688463543053, "user_tz": -180, "elapsed": 1274, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))
img0=img.transpose(1,0,2)
plt.imshow(img0)
plt.title("Повернутое транспонированное изображение")
```

<!-- #region id="_OouRtRVikb0" -->
5. Переворот изображения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 452} id="lNouzwnkilLt" outputId="43e35afa-998a-4092-b5d3-b61f1a0a3840" executionInfo={"status": "ok", "timestamp": 1688463553522, "user_tz": -180, "elapsed": 1576, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

img0 = img.copy()

for i in range(img0.shape[0] // 2):
    c = img0[i, :, :].copy()
    img0[i, :, :] = img0[img0.shape[0] - i - 1, :, :]
    img0[img0.shape[0] - i - 1, :, :] = c

plt.imshow(img0)
```

<!-- #region id="fXzIK_N-fChM" -->
6. Негатив изображения.


<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 365} id="WyMRjzUofHpT" outputId="11a22516-0628-4eba-a6f0-e585e18f7b0a" executionInfo={"status": "ok", "timestamp": 1688463584121, "user_tz": -180, "elapsed": 2067, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

fig = plt.figure(figsize=(10, 10))
fig.add_subplot(1, 2, 1)
plt.imshow(img)
plt.title('Оригинал')

img = 255 - img
fig.add_subplot(1, 2, 2)
plt.imshow(img)
plt.title('Негатив RGB изображения')
```

<!-- #region id="0gXosn_HfcR2" -->
7. Создание окантовки изображения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 452} id="dCRBMbVIffW8" outputId="816b7e9c-e176-4007-812b-297053a5a5c3" executionInfo={"status": "ok", "timestamp": 1688463593367, "user_tz": -180, "elapsed": 1167, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))
img_gray = img.sum(2) / (255*3)
img0 = img_gray.copy()
img0 = np.pad(img0, ((100,100),(100,100)), mode='constant')
plt.imshow(img0)
img0.shape, img.shape
```

<!-- #region id="t83Ca9cBfrui" -->
8. Визуализация  RGB-каналов.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 268} id="-VikZAScfqyL" outputId="226f5d8f-a9f4-4fd9-c991-f4d2d997e246" executionInfo={"status": "ok", "timestamp": 1688463630574, "user_tz": -180, "elapsed": 1530, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

img_R, img_G, img_B = img.copy(), img.copy(), img.copy()

img_R[:, :, (1, 2)] = 0
img_G[:, :, (0, 2)] = 0
img_B[:, :, (0, 1)] = 0



img_rgb = np.concatenate((img_R,img_G,img_B), axis=1)
plt.figure(figsize=(15, 15))
plt.imshow(img_rgb)
```

<!-- #region id="7IGhDeC4fzFz" -->
9. Снижение яркости.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 268} id="etzDREyKf2JM" outputId="9c170a7f-52a2-4461-b079-8cad930ff944" executionInfo={"status": "ok", "timestamp": 1688463658276, "user_tz": -180, "elapsed": 2166, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

# Деление значения пикселей на число, получение значений типа int после округления и затем умножение на то же число

img_0 = (img // 64) * 64
img_1 = (img // 128) * 128

img_all = np.concatenate((img, img_0, img_1), axis=1)

plt.figure(figsize=(15, 15))
plt.imshow(img_all)
```

<!-- #region id="E_HpmIghK3C4" -->
10. Бинаризация изображения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 268} id="NUH880Q6gqIr" outputId="fcc40d32-7f90-4669-ad3a-a5d74a579980" executionInfo={"status": "ok", "timestamp": 1688463679920, "user_tz": -180, "elapsed": 2297, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

img_64 = (img > 64) * 255
img_128 = (img > 128) * 255

fig = plt.figure(figsize=(15, 15))

img_all = np.concatenate((img, img_64, img_128), axis=1)
plt.imshow(img_all)
```

<!-- #region id="PzjOqhrjgyvY" -->
11. Смешивание двух изображений.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 691} id="4JcTdjRKg1oR" outputId="8a626df0-6611-4a05-f6f3-38283776af06" executionInfo={"status": "ok", "timestamp": 1688463702738, "user_tz": -180, "elapsed": 3582, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))
img0 = np.array(Image.open('mountains.jpeg').resize(img.shape[1::-1])) # изменение размеров второго изображения (по ширине, по высоте)

print(img.dtype)


dst = (img * 0.6 + img0 * 0.4).astype(np.uint8)   # смешивание

plt.figure(figsize=(10, 10))
plt.imshow(dst)
```

<!-- #region id="IguYgyZxirpT" -->
12. Построение гистограммы интенсивности пикселей.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 472} id="PvVVx4P5itbj" outputId="0669c706-aab4-4ea9-af9c-b58a8698a434" executionInfo={"status": "ok", "timestamp": 1688463760002, "user_tz": -180, "elapsed": 1441, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
img = np.array(Image.open('dog.jpg'))

img_flat = img.flatten()

plt.hist(img_flat, bins=200, range=[0, 256])
plt.title("Number of pixels in each intensity value")
plt.xlabel("Intensity")
plt.ylabel("Number of pixels")
plt.grid()
plt.show()
```

<!-- #region id="mkui-YPWy8CN" -->
**Выводы**:

1. Библиотека `NumPy` позволяет работать с изображениями, представляя их в формате матриц: проводить основные операции с изображением в виде RGB, получать статистику по значению яркости пикселей изображения.
2. Изученные операции могут быть полезны не только для обработки изображений в контексте машинного обучения, но и для создания признаков и разметки.
<!-- #endregion -->
