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

<!-- #region id="OY_nQJ24-6Lu" -->
# Получение и предобработка данных. Первичная работа с объектом DataFrame
<!-- #endregion -->

<!-- #region id="k97-gJWJBB9A" -->
Этот ноутбук содержит примеры кода для предобработки данных в Python и первичной работе с объектом `DataFrame`.

К основным частям кода мы прописали текстовые пояснения, если же они покажутся недостаточными, пожалуйста, обратитесь к материалам лекции в LMS.
<!-- #endregion -->

<!-- #region id="PKWQI-DX--nv" -->
## Предобработка данных с использованием библиотеки `Pandas`
<!-- #endregion -->

<!-- #region id="ixIPb8USA4X-" -->
Импорт библиотеки `Pandas` и чтение данных из файла. Чтобы не писать имя библиотеки полностью, мы сократили ее название как `pd`.

**Важно!** Прежде чем выполнять код, загрузите файл `train.csv`.
<!-- #endregion -->

```python id="krIUELdaEkCM"
import pandas as pd
```

```python id="RPQzxRk97Z2V"
df = pd.read_csv('train.csv')
```

<!-- #region id="mm70B65gA8ve" -->
Выводим первые 5 строк
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="dowrs-AM-00o" outputId="570e87f1-e7a7-416e-9f1f-ccc5d8596ca3"
df.head()
```

<!-- #region id="odm2zYXwFMx4" -->
Получаем информацию о данных.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="Wxj6elIPA28o" outputId="afad8096-eae3-46fa-e5c3-426e738ce963"
df. info()
```

<!-- #region id="7UfB1pH0FVHn" -->
Определяем, есть ли в данных пропущенные значения
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="epNl69JAFVYP" outputId="e315ee33-0623-440e-d7dc-40576fdf2b7a"
df.isnull().sum()
```

<!-- #region id="E-pdwgXGFkaS" -->
Заменяем пропуски в данных на средние значения.
<!-- #endregion -->

```python id="Y3s6SeiVFky5"
df["Age"].fillna(df["Age"].mean(), inplace = True)
```

<!-- #region id="FgeK61GrF5BJ" -->
Снова смотрим, есть ли в данных пропущенные значения.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="9p1mfKnDF5T0" outputId="b6857461-3c10-4e2b-a9bb-118e109ff40c"
df.isnull().sum()
```

<!-- #region id="swu407uqF-Q5" -->
Проверяем, содержатся ли в данных строки-дубликаты.
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="l3WshJeWF-gp" outputId="09a739fd-a135-4fa0-ab8d-3c0aa5c683fd"
df.duplicated()
```

<!-- #region id="eRVV8Eec_Td1" -->
## Первичная работа с `DataFrame`
<!-- #endregion -->

<!-- #region id="x_2ROd076ZWr" -->
В Pandas есть два главных типа данных — `DataFrame` и `Series`. Тип данных `Series` — достаточно простой. Как правило, он передается с помощью списка, состоящего из последовательности каких-то символов.
<!-- #endregion -->

<!-- #region id="RTTwkC3A7G8k" -->
Создадим `DataFrame`, используя функцию `pd.DataFrame`:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="ksF0jo1V7Kwc" outputId="c06115b2-48b6-4086-ae1c-f444d31f8e57"
pd.DataFrame({'Column 1': ['Black', 50], \
          	'Column 2': [155, ['orange','apple']]})
df
```

<!-- #region id="NoIPH9fT83RF" -->
### Атрибуты датафрейма
<!-- #endregion -->

```python id="FN4A--MgAeUG"
df = pd.read_csv('fruits.csv')
```

<!-- #region id="hYGpDZc67vt8" -->
Число измерений датафрейма:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="p-L_rbpl7yVW" outputId="4bb8da07-a5bb-4c8e-b12c-8152f5abb021"
df.ndim
```

<!-- #region id="94df6YwG7vwE" -->
Размерность датафрейма:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="_z4h6aSa8HJ8" outputId="28614f60-de73-4d06-a0ab-caeef800715a"
df.shape
```

<!-- #region id="pCIOQh4F7vyO" -->
Число ячеек:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="I2erfWxD7yd8" outputId="7a0d2fb1-198d-4323-b5d8-edc8389157e7"
df.size
```

<!-- #region id="vKZFiHBb7v6F" -->
Информация о названии колонок:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="rej4m0fP8iCU" outputId="6cee2d3c-62aa-456c-a2ce-4ecb053a8148"
df.columns
```

<!-- #region id="-TeDX33H8hKq" -->
Информация о названии осей:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="VpM9ivPH8uks" outputId="0602ca4d-8791-4a34-ac14-408f828ce544"
df.axes
```

<!-- #region id="vFgx4HHm8hd8" -->
Типы данных для каждой из колонок:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="B1Mhl7Pr7woj" outputId="9538ca56-9e49-498b-a380-034675f2fb0c"
df.dtypes
```

<!-- #region id="zV23ST7n8-gC" -->
### Первичное исследование датафрейма
<!-- #endregion -->

<!-- #region id="9zX5v1I09DGi" -->
Для первичного исследования датафрейма будут полезны три функции:
*   `head(n)` — вывод первых *n* строк датафрейма;
*   `tail(n)` — вывод последних *n* строк датафрейма;
*   `describe()` — вывод описательных статистик (только для колонок типа `float` и `int`).

<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="dFMSjq1d9WxN" outputId="9844dbf1-bc55-44d5-de31-ab7ce4b90b32"
df.head()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="fMhO6Eo89Yis" outputId="d20755eb-07e2-4eee-b174-30346ab81f51"
df.tail()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 300} id="u9YSAIaf9ZCb" outputId="b3f6ad30-2cba-4723-982f-3487f11801d1"
df.describe()
```

<!-- #region id="_C2B3QqE9T31" -->
### Индексирование
<!-- #endregion -->

<!-- #region id="yDmqHuKY9pQE" -->
Чтобы сослаться на конкретную ячейку, нужно сначала сослаться на название колонки, а потом — на индекс строки:
*   `df.column_name[index]`;
*   `df['column_name'][index]`.
<!-- #endregion -->

<!-- #region id="i90bpYTN91Lt" -->
Первый способ:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="EpBEixkZ97pV" outputId="446d84bf-5f58-439b-aa0d-eade7055c8a3"
df.total[0]
```

<!-- #region id="7ru88wif95z2" -->
Второй способ:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="tpErPR8d98If" outputId="9e5aee5b-4add-4995-9888-4f0b730fec98"
df['total'][0]
```

<!-- #region id="cZLDviLaA1TO" -->
Пример ссылки на несколько ячеек:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="fMxHloh9A1sd" outputId="e1035630-c1db-45c3-ad32-dbfaa7b23da0"
df['total'][0:2]
```

<!-- #region id="r7wPVruoA8st" -->
Два основных способа осуществления срезов:
*   по индексу: `iloc[start:stop:step, start:stop:step]`
*   по лейблу: `loc[start:stop:step, [column_names]]`

<!-- #endregion -->

<!-- #region id="wRSJf1o9BMu3" -->
Вывод элементов первой строки первого столбца.
<!-- #endregion -->

<!-- #region id="KuYvS1zOBR72" -->
Первый способ:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 36} id="3fmpWneuBUs0" outputId="a48ea9f0-32cd-427e-eac6-d4b4596043b8"
df.iloc[0,0]
```

<!-- #region id="qJVXjJ_RBTHo" -->
Второй способ:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 36} id="9QTjjJH3BIQX" outputId="7dc9bdf2-42b2-4d5a-9b2b-b3e4db152c28"
df.loc[0,'fruit']
```

<!-- #region id="9BrSB4utBj8j" -->
Вывод первых двух строк первых двух столбцов:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="NXRvcLAuBnvM" outputId="fcad001a-bffb-440d-d808-a0e401c41887"
df.iloc[0:2,0:2]
```

<!-- #region id="eZLGNlTIC1RV" -->
Пример использования метода `loc`:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="0t0hc2L-C5h3" outputId="668b6718-a821-4e2e-de76-1d5dd6efc7a4"
df.loc[0:2,['fruit', 'shop']]

```

<!-- #region id="YXfS-ddqDKXd" -->
### Срез по условию
<!-- #endregion -->

<!-- #region id="2KYjky8TDSmk" -->
Схема осуществления среза по условию:
`df.loc[condition_2 &/| condition_2 &/|…&/| condition_3]`.


Нужно выбрать транзакции с лимонами на общую стоимость более 8 у. е.:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="ouR4UENzDPPE" outputId="beecd9ae-df0c-44c3-ca2a-b0684d035b59"
df.loc[(df.total > 8) & (df.fruit == 'lemons')]
```

<!-- #region id="-hX_VQ_nDcxV" -->
## Введение в агрегирование и сводные таблицы
<!-- #endregion -->

<!-- #region id="skEN1Z4NDik8" -->
**Агрегирование** — обобщение вложенных структур данных.

Агрегирование можно осуществить с помощью метода `groupby()`.
Общая схема может выглядеть так:
`groupby('grouping_variable')['aggregation_variable'].method_aggregation()`

В показанной схеме:
*   `grouping_variable` — переменная группировки;
*   `aggregation_variable` — переменная агрегирования;
*    `method_aggregation()` — метод агрегирования.
<!-- #endregion -->

<!-- #region id="Wvdk2RALDxs9" -->
Задача — узнать среднюю стоимость покупок фруктов для каждого магазина:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="dh5Ti1qDD4OE" outputId="631d74ee-6d10-40a7-a618-cc72b85c0229"
df.groupby('shop')['total'].mean().reset_index()
```

<!-- #region id="qFior4tTD98U" -->
Сводные таблицы удобно реализовывать с помощью метода `pivot_table()`.
<!-- #endregion -->

<!-- #region id="X8DaOLLEEAgU" -->
Задача — получить сумму стоимостей покупок для каждого вида товара в каждом магазине с разбиениями по платформе:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="9sEiZa5iEAU1" outputId="308185d0-f2a8-4c7d-ec5f-e5536a6b2fe4"
import numpy as np

pd.pivot_table(df, \
    	values='total', \
    	index=['fruit', 'shop'],\
    	columns=['pl'], \
    	aggfunc=np.sum)
```

<!-- #region id="Vwod6fBEEXcl" -->
**Методы агрегирования:**
*   `count()` — общее число наблюдений
*   `first()`, `last()` — первое и последнее наблюдения
*   `mean()`, `median()` — среднее и медиана
*   `min()`, `max()` — минимум и максимум
*  `std()`, `var()` — стандартное отклонение и дисперсия
*  `mad()` — среднее абсолютное отклонение деление
*  `prod()` — произведение всех наблюдений
*  `sum()` — сумма всех наблюдений


<!-- #endregion -->
