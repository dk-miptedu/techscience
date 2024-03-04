# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="OoN8iUzDK01b"
# # Библиотека NumPy

# + [markdown] id="s1rp_Ow7K1k6"
# Этот ноутбук содержит примеры кода для работы с библиотекой `NumPy`.
#
# К основным частям кода мы прописали текстовые пояснения, если же они покажутся недостаточными, пожалуйста, обратитесь к материалам лекции в LMS.

# + [markdown] id="pVYIFgGmLgVD"
# Импортируем библиотеку.

# + id="GbhSwqTEKvJh"
import numpy as np

# + [markdown] id="M3xOW3SeWkNP"
# ## Массивы NumPy

# + [markdown] id="xAqbm73yOCzr"
# ### Создание массива

# + [markdown] id="joSGMXFZLj8j"
# Создадим одномерный массив из чисел 1, 2, 3.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 15, "status": "ok", "timestamp": 1677000659674, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="x-gagZiDLkPS" outputId="089790ab-ea32-43c3-c67c-9e45e0a4e091"
np.array([1,2,3])

# + [markdown] id="4iYfIfWmLkY7"
# Создадим двумерный массив.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 13, "status": "ok", "timestamp": 1677000659675, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="cQ0oSCAcLkiU" outputId="8c2acdf8-4149-4829-8d16-eed618a4d685"
a = np.array([[1, 2, 3], [4, 5.0, 6]])
print(a)

# + [markdown] id="gsoylY-8LkuK"
# Получаем атрибуты массива:
# *   `ndarray.ndim` — число измерений матрицы. Для строки это 1, для матрицы — 2.
# *   `ndarray.shape` — размеры массива, его форма. Размер каждого из осей многомерного массива.
# *   `ndarray.size` — количество элементов массива.
# *   `ndarray.dtype` — объект, описывающий тип элементов  массива.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1677000659675, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="uTFoTk7qNX50" outputId="93c19275-2631-47bc-c02f-2bf1f58f1d5a"
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# + [markdown] id="gTwpber0NksS"
# Создаем массив на основе генерации последовательности.
#
# `np.arrange(начало, конец, шаг)` — генерация последовательности на интервале, аналогично функции `range()`.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1677000659676, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="LSj-OQcrNk9L" outputId="1936892f-689b-4a03-9365-4a9c1b5f9fb1"
a = np.arange(0,10,2)
print(a)

# + [markdown] id="Mrlx04ZuOMSs"
# `np.linspace(начало, конец, число_элементов)` — генерация последовательности на интервале, но вместо шага указываем, сколько элементов массива нужно создать (конец включается).
#

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1677000659676, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="_9nHRdQGOMkk" outputId="8932f12e-04a6-4649-f9ba-3e257f0778a3"
b = np.linspace(0,10,5)
print(b)

# + [markdown] id="DUZve77HOfHK"
# Частные способы создания массивов:
# *   `np.zeros()` — создание массива из нулей.
# *   `np.ones()` — создание массива из единиц.
# *   `np.eye()` — создание единичной матрицы. Это квадратная матрица, заполненная нулями, кроме главной диагонали — от левого верхнего до правого нижнего элемента, которая заполнена единицами.

# + [markdown] id="yqMBTq-zOtmU"
# ### Индексирование массива

# + [markdown] id="hCKX3vZuPB57"
# Система индексирования одномерных массивов аналогична спискам. Необходимо сослаться на массив и в квадратных скобках указать индекс или серию чисел — начало, конец и шаг:
#
# `your_array[начало:конец:шаг]`

# + [markdown] id="Lx1ZwEvpPNwL"
# Исходный массив.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1677000659677, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="PV1G9PJLPIDn" outputId="15b7d0e7-5cd5-4ca1-a0b1-5973af07df4e"
a = np.array([[1, 2, 3], [4, 5.0, 6]])
a

# + [markdown] id="rX_N91UtPXJ0"
# Сошлемся на первый элемент первой строки.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 466, "status": "ok", "timestamp": 1677000660133, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="PU8pGXpdPXQ-" outputId="7d878fa7-ea50-4b80-b084-f31a3bc49795"
a[0,0]

# + [markdown] id="fui3sI_GPXoi"
# Заменим элемент первой строки первого столбца.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1677000660133, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="Fzhm_40WPX6n" outputId="a13a4746-02ec-458e-d7ed-eee830a7cce1"
a[0][0] = 1.5
a

# + [markdown] id="QPzSJdr1QyQL"
# Замена первого столбца в матрице.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1677000660134, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="mL7iYvlOQyhZ" outputId="1a904b3c-959b-4bfc-e9bc-97f788d5494f"
a[:,0] = [0, 1]
a

# + [markdown] id="mn0klPiFUOpw"
# Замена первой строки.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1677000660135, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="VjYOG9ulUSmb" outputId="f5e10bcf-f10c-44ac-ae5b-c711027eb04f"
a[0,:] = [1,2,3]
a

# + [markdown] id="dIkKQr_SRFGk"
# ### Удаление элемента из массива

# + [markdown] id="gC0hEeH-RFPV"
# Удалить элементы из массива можно с помощью метода `np.delete(объект, индекс(ы), ось)`:
# *   объект — массив;
# *   индекс(ы) — индекс или список индексов;
# *   ось — по умолчанию `axis = 0`.

# + [markdown] id="mJ2kgGI1Utv_"
# Другой способ — сделать срез и пересохранить массив.

# + [markdown] id="6Z3GSZK9UyoH"
# Например, нам нужно удалить последний элемент в массиве.
# 1-й способ.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1677000660135, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="FCJ7Aw5kU-QS" outputId="dc7d7725-eb1c-4358-c71e-ee4e04a8c11b"
a = np.array([1,2,3,0])
a1 = np.delete(a, 3)
print(a1)

# + [markdown] id="D9zW4JMBVLjW"
# 2-й способ.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1677000660136, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="gPAAnOsZVM0e" outputId="bb9a9b1a-bb91-48ac-961c-be567f2da176"
a2 = a[0:3]
print(a2)

# + [markdown] id="2brhANaSVRuO"
# Метод `np.reshape()` позволяет изменить размерность массива.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 10, "status": "ok", "timestamp": 1677000660136, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="2t9fGn1YVjXZ" outputId="e4de0157-c2bd-4099-de74-8d6d4cc7de35"
# исходный массив — [1, 2, 3, 4, 5, 6]
np.array([1, 2, 3, 4, 5, 6]).reshape(3,2)

# + [markdown] id="o6Ut-u7NVyt4"
# ### Транспонирование массива

# + [markdown] id="tD8RCy31V2cP"
# В `NumPy` можно транспонировать массив любой размерности с помощью метода np.`transpose()`

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 9, "status": "ok", "timestamp": 1677000660137, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="BnAI2PG8WFD2" outputId="8b7f3c12-f4b3-477f-b02b-b82dee3917c2"
a = np.array([[0, 1, 2], [4, 5, 6]])
a = a.transpose()
print(a)

# + [markdown] id="ugVbLwYwWwxE"
# ## Работа с векторами

# + [markdown] id="Tz0q1m1IW1UM"
# Массивами `NumPy` поддерживаются арифметические операции основного Python:
# *   сложение +
# *   вычитание –
# *   нахождение равенства =
# *   деление /
# *   целочисленное деление //
# *   возведение в степень **
# *   и т. д.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 300, "status": "ok", "timestamp": 1676998836514, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="QlqdS4AJzvSW" outputId="c528bd35-0637-49be-e1e9-df95f776a1cb"
# сложение, массив + число
x = np.array([0,1,2,3])
x + 5

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 293, "status": "ok", "timestamp": 1676999222212, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="ybGmoy7OzvTi" outputId="c5d9ded7-661a-4070-befd-cd2c4e54674d"
# сложение массивов
x = np.array([0, 1, 2, 3])
y = np.array([4, 5, 6, 7])
x + y

# + [markdown] id="ixnsgSZs8ons"
# ### Нормализация векторов
# **Нормализация переменных** — приведение вектора чисел к стандартизированному виду.

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 974, "status": "ok", "timestamp": 1676999353055, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="j6d_PCkD8awb" outputId="82ee1e19-5848-499a-8c7a-f1278b06319d"
heights = np.array([187, 188, 190, 177, 156, 189])

print((heights- np.min(heights)) / (np.max(heights) - np.min(heights)))

# + [markdown] id="Ewq88-nN-vqb"
# ### Скалярное произведение векторов
# В экономике часто можно наблюдать скалярное произведение вектора цен на вектор количества проданных товаров. Скалярное произведение в этом случае дает стоимость всех проданных товаров.

# + [markdown] id="mvc_pesJ_Rnq"
# ![image.png](data:image/png;base64,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IiIikhkWAUREREREMsMigIiIiIhIZlgEEBERERHJDIsAIiIiIiKZYRFARERERCQzLAKakBAC//jHP7B7926z+5SVleG9995DaWmpBSMjIiIiIvp/TVYELF26FP369cO5c+eMtgshsG3bNjg7OyM5ORnV1dVN9SsfKkIIpKenY8WKFfDy8jK7X7t27eDq6oro6GiUlJRYMMLmTafTITs7G3/5y19w/vz5WtsUFBQgKioKCoUCzs7OGDduHH7++WeTdiqVCgkJCejVqxckSYK/vz+2b98OnU5n6ZdBDxlz8mr16tWQJMnkMWLECJSXlxvaMa+ouroa3333HV588UU4OztDoVAgKioKBQUFJm05XpG5avIqKCgIkiTB09MTixYtqvXgIccragw7S/+CgwcPYsGCBXjttdcwceJE2Ni0zJMP+fn52LhxIz788EP4+PiY3c/Ozg4RERHIzc3FF198gVmzZsHOzuJ/lmbj1q1b2LVrFzZs2IAff/wRvr6+mDZtmkm7goICTJw4EZ07d8bWrVthb2+P1NRUvPLKK9i+fTuefPJJAIBWq8W7776L7777DnPnzkW3bt1w+PBhvP3221AqlZgyZQokSXrQL5MeMHPzCgBu376NgIAAjBgxAo888ohhe9u2bdGqVSsAzCu6eyBo+/btmD17NmJiYjB79myoVCokJiYiPDwcKSkp6NGjBwCOV2S+e/Nq+vTpWLRoEW7duoXExERER0cjOTkZHTp0MLTneEWNIhpgRhMhhBBLliwRvr6+Ij8/37Dt7Nmzws/PT4SEhIji4mKz9tMcVVZWilmzZokFCxaIO3fu/K59HDlyRPTu3VscPXq0iaN7ODUmrzw8PMSSJUtESkqKSY7V2LBhg/Dz8xMXL140bCspKRGjR48WcXFxQqfTCSGEOHnypOjRo4fIzMw0tNPpdOJvf/ubCAoKEkVFRff5ysiamjqv1Gq1iI6OFu+++66orq6uc3/Mq5bNnLwqKCgQQ4cOFatWrTLKlZMnTwofHx/xySefGLZxvCIhzMurq1evisDAQJO8On78uOjRo4f45z//adjG8YqEMP9zUAghLHZYXqVSYd26dQCA5cuXw83Nzeh5jUaDDRs2wN/f33AqKj09HVqt1qRdTExMrae30tLS6o0hOzvbpI+npyeio6NrPT176tQpvPnmm1AoFPWexv2tCxcu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w3uaOUm16d69OyZMmIB58+ahvLwc/v7+UKlU2LJlC6qqqvDSSy9ZO0RqhmxtbREWFoaMjAzMnDkTEydOhEajQWJiInr27ImgoCBDW45X1GiiAWY0EUIIsWTJEgHArMehQ4cM/dRqtVi/fr3w8/MTAISfn59ISkoSt2/fNjwfHR0toqOjheJq8osAAALKSURBVFqtNupX2/YTJ06I0NBQw77S09PFpk2bRN++fUVeXl6d8RcVFYmgoCCRmppqtD01NVX4+vqKvXv3isjISOHi4iI8PDxEfHy80e+9N6a4uDih0+nM+n+TK3PzSgghLl26JGJjY4WHh4dwcnISY8aMEfv37xfV1dUWjJCaI3PyKj8/X/j6+po1RiUlJQl/f3/xyy+/GO2DOSkv5o5XlZWVIiMjQwwfPlwAEB4eHiI2NlZcunTJwhFSc9SYz8ETJ06Il19+WTg5OQkXFxcRGRlpklccr0iIxuWV9L8OdZIkqcluKJGdnY1hw4bh0KFDDV6L+0ETQmDNmjU4fvw41q5da7hrcFpaGlauXIkvv/zS5Kj/b+Xm5iIqKgrr1q3DoEGDHkTYzVZT5hVRDeYVWQLziiyBeUWW0Ji8suodgx8mkiQhPDwcSqUSe/bsaXR/rVaLrVu3IjQ0FP369bNAhERERERETYNFwD3c3NwwY8YMJCcnN+qSojqdDqmpqbhy5QomTZp0X5cZJCIiIiKytAf6bTUgIOChP/X17LPPYvny5Th+/DgGDBhgVp+KigpcvnyZd4UkIiIiombhga4JIKrBvCJLYF6RJTCvyBKYV2QJXBNARERERER1YhFARERERCQzLAKIiIiIiGSGRQARERERkcywCCAiIiIikhkWAUREREREMsMigIiIiIhIZlgEEBERERHJTL03C5Mk6UHGQkRERERE98Hcm4XZNcVOiIiIiIio+eB0ICIiIiIimWERQEREREQkMywCiIiIiIhkhkUAEREREZHMsAggIiIiIpIZFgFERERERDLDIoCIiIiISGZYBBARERERyQyLACIiIiIimWERQEREREQkMywCiIiIiIhkhkUAEREREZHMsAggIiIiIpIZFgFERERERDLDIoCIiIiISGZYBBARERERyQyLACIiIiIimfk/7fOOO7jDP5sAAAAASUVORK5CYII=)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 305, "status": "ok", "timestamp": 1677000136480, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="y76dWSA08oPr" outputId="22aa45c5-2202-4116-ef37-b270106bb335"
# вектор проданных товаров
q = np.array([100, 150, 200, 350])

# вектор цен
p = np.array([5, 2.5, 3, 0.5])

np.dot(q, p)

# + [markdown] id="kwtXY_z8ANB2"
# ### Решение системы линейных уравнений
# Рассмотрим в качестве примера следующую систему уравнений:
#
# 20x+10y=350
#
# 17x+22y=500

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 339, "status": "ok", "timestamp": 1677000648714, "user": {"displayName": "\u041d\u0430\u0434\u0435\u0436\u0434\u0430 \u0422\u0443\u043f\u0438\u043a\u0438\u043d\u0430", "userId": "16854253095026240007"}, "user_tz": -420} id="qR21CTLyAgTT" outputId="040ca098-cd3e-4d8a-cdd2-da74cffedea0"
A = np.array([[20, 10], [17, 22]])
B = np.array([350, 500])

X = np.linalg.solve(A,B)
print(X)
