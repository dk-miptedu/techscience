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

<!-- #region id="uMV3UW_GOpbb" -->
# Анализ данных с Pandas
<!-- #endregion -->

<!-- #region id="n34XdA0aOpbh" -->
## Часть 1. Базовые операции с `DataFrame`

**Pandas** — программная библиотека на языке Python для обработки и анализа данных. Работа `pandas` с данными строится поверх библиотеки `NumPy`, являющейся инструментом более низкого уровня.
Библиотека оптимизирована для высокой производительности, наиболее важные части кода написаны на `Cython` и `С`.

Главные структуры данных в `Pandas`:
 - `DataFrame` — двумерный неоднородный индексированный массив, таблица;
 - `Series` — одномерный индексированный массив ndarray, столбец/строка;
 - `Index` – индекс (список названий строк/столбцов).
<!-- #endregion -->

<!-- #region id="oEsU-a9nOpbj" -->
###Настройка отображения
[Документация set_option](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html)
<!-- #endregion -->

<!-- #region id="TokW8uMkOpbk" -->
Подключим библиотеку. Обычно для этой библиотеки используют сокращение `pd`.
<!-- #endregion -->

```python id="EugI_MRxOpbl"
import pandas as pd
```

<!-- #region id="OW2_QB7SOpbp" -->
Проверим версию `pandas`:
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="cPL0rEWYOpbq" executionInfo={"status": "ok", "timestamp": 1675957304606, "user_tz": -180, "elapsed": 779, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="5ea12542-08ed-41a4-8f8c-beff6d19cd8c"
print(pd.__version__)
```

<!-- #region id="SZNTovOwOpbr" -->
Настроим опции отображения с помощью функции `set_option`:
<!-- #endregion -->

```python id="51c9XncWOpbs"
# максимальное количество отображаемых столбцов
pd.set_option('display.max_columns', 13)
# максимальное количество отображаемых строк
pd.set_option('display.max_rows', 10)
# максимальная ширина столбца
pd.set_option('display.max_colwidth', 45)
# максимальная ширина отображения
pd.set_option('display.width', 80)
```

<!-- #region id="QYngdyJpOpbt" -->
###Чтение данных из файла

[Документация read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
<!-- #endregion -->

<!-- #region id="AJmw4ML5Opbu" -->
Табличные данные чаще всего представлены в формате **csv** (**C**omma-**S**eparated **V**alues – "значения, разделенные запятыми").
<!-- #endregion -->

<!-- #region id="SM6zkYjaOpbu" -->
Загрузим данные, например из csv-файла. Это можно сделать с помощью функции `read_csv` из библиотеки `pandas`.

В этом ноутбуке мы будем использовать таблицу из датасета [Top 100 popular movies from 2003 to 2022 (iMDB)](https://www.kaggle.com/datasets/georgescutelnicu/top-100-popular-movies-from-2003-to-2022-imdb), содержащего данные о 100 самых популярных фильмах каждого года с 2003 по 2022 года. Очень много других датасетов для тренировки и не только вы можите найти на [kaggle](https://www.kaggle.com/datasets).
<!-- #endregion -->

<!-- #region id="iofe1PoNOpbv" -->
**Описание данных**
<!-- #endregion -->

<!-- #region id="7XpGLS_NOpbv" -->
Источник данных - iMDB
<!-- #endregion -->

<!-- #region id="unK3ahaIOpbw" -->
Variable | Definition
---|---------
Title | Название фильма
Rating | Оценка на iMDB
Year | Год выхода фильма
Month | Месяц выхода фильма
Certificate | Возрастной рейтинг
Runtime | Продолжительность
Director/s | Режиссер/ы
Stars | Актеры, играющие в фильме
Genre/s | Жанр/ы фильма
Filming Location | Место съемки фильма
Budget | Бюджет фильма
Income | Сборы фильма
Country of Origin | Страна-производитель фильма
<!-- #endregion -->

```python id="fG5sB6y5Opbw"
data = pd.read_csv("movies.csv", sep=',')
```

<!-- #region id="av7Zu0-zx3nZ" -->
Так же можно использовать файл из вашего google диска:
<!-- #endregion -->

```python id="evl_FWO0vc00"
from google.colab import drive
drive.mount('/content/drive')
```

<!-- #region id="oQ0VXaaFOpbx" -->
Часто в `read_csv` нужно указать:
   - разделитель полей `sep` (по умолчанию  ',');
   - кодировку encoding (например, `'utf8'`, в Windows часто бывает `'cp1251'`);
   - разделитель дробей `delimiter`;
   - `usecols` — какие колонки нужно загрузить (бывает, что нужны не все, особенно актуально, когда данных много)
   - `index_col` — колонка–индекс;
   - `dtype` — словарь, задающий типы данных для соответствующих полей;
   - и т.д.
<!-- #endregion -->

<!-- #region id="zeBIdNedOpbx" -->
У функции `read_csv` множество параметров. Чтобы посмотреть полный список можно воспользоваться справкой: знак вопроса и имя функции или найти описание на [сайте документации](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
<!-- #endregion -->

```python id="1-FyWRXbOpby"
pd.read_csv?
```

<!-- #region id="W1vw-DY0Opby" -->
Мы считали данные в объект типа `DataFrame`:
<!-- #endregion -->

```python id="IupIJf90Opbz" outputId="07333f98-809a-47d1-a997-9a63ccab715a" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675957631737, "user_tz": -180, "elapsed": 386, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
type(data)
```

<!-- #region id="EyaQWIOYOpbz" -->
#### Просмотр данных
<!-- #endregion -->

<!-- #region id="nMZ_Ke4nOpb0" -->
Посмотрим первые 5 строк нашей таблицы:
<!-- #endregion -->

```python id="2ifElIofOpb0" outputId="7db1b205-2e71-4402-ecef-90563633b0e4" colab={"base_uri": "https://localhost:8080/", "height": 617} executionInfo={"status": "ok", "timestamp": 1675957655100, "user_tz": -180, "elapsed": 399, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.head()
```

<!-- #region id="zyt3Vn5WOpb0" -->
Если нужно посмотреть первые **n** строк, то нужно просто это явно указать. *Не забываем использовать подсказку (навидите курсор на функцию и нажмите shift+tab, это работает только после импорта библиотеки)*
<!-- #endregion -->

```python id="a7d7x9HsOpb1" outputId="78d8782e-5c70-408f-b8fc-b7908b5091e4" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675957684445, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.head(10)
```

<!-- #region id="GQ4KKO98Opb1" -->
Посмотрим последние 5 строк нашей таблицы:
<!-- #endregion -->

```python id="kTJ3kZS9Opb1" outputId="df0c06aa-3ed9-421a-83c7-81bb28559cf0" colab={"base_uri": "https://localhost:8080/", "height": 600} executionInfo={"status": "ok", "timestamp": 1675959297581, "user_tz": -180, "elapsed": 606, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.tail()
```

<!-- #region id="KT53eIBxOpb2" -->
Посмотрим случайные n строк:
<!-- #endregion -->

```python id="irQPgumEOpb2" outputId="ed0a42de-ba74-4ee7-d2bb-d3c4258aeb10" colab={"base_uri": "https://localhost:8080/", "height": 467} executionInfo={"status": "ok", "timestamp": 1675957733403, "user_tz": -180, "elapsed": 387, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sample(n=3)
```

<!-- #region id="XG5SOsE0Opb2" -->
#### Размер данных
<!-- #endregion -->

```python id="JynviSohOpb3" outputId="975315ba-7ee8-4bed-ece7-233e5e73b80a" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675957756191, "user_tz": -180, "elapsed": 774, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.shape
```

<!-- #region id="9ThKRV30Opb3" -->
#### Описательные статистики
<!-- #endregion -->

<!-- #region id="NQWypVM_Opb3" -->
Чтобы получить описание по численным данным, можно воспользоваться методом `describe()`:
<!-- #endregion -->

```python id="Klfd_HHtOpb6" outputId="ef0e2e9a-af3f-416b-d226-a454f3aca7f1" colab={"base_uri": "https://localhost:8080/", "height": 300} executionInfo={"status": "ok", "timestamp": 1675957797559, "user_tz": -180, "elapsed": 393, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.describe()
```

<!-- #region id="PCnklG3ZOpb6" -->
####  Информация о данных
<!-- #endregion -->

<!-- #region id="Y3GheiMVOpb6" -->
Чтобы посмотреть, какие есть признаки, какой у них тип данных в таблице, сколько есть заполненных ячеек, воспользуемся методом `info()`:
<!-- #endregion -->

```python id="P2CCBVfHOpb7" outputId="502fd2a9-1a82-4198-d650-2c2b46816085" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675957820167, "user_tz": -180, "elapsed": 397, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.info()
```

<!-- #region id="y482C60rOpb7" -->
###Индексация
<!-- #endregion -->

<!-- #region id="TjMFQ8yTOpb7" -->
Подробнее про индексацию вы можете посмотреть в [документации](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).
<!-- #endregion -->

<!-- #region id="EBG5P6pyOpb8" -->
Общий подход
- Индекс + столбцы
 - элемент  **`data.loc[index, column]`**
 - подтаблица **`data.loc[list of index, list of columns]`**
<!-- #endregion -->

<!-- #region id="jlSrtW4UOpb8" -->
- По нумерации строк и столбцов
 - элемент  **`data.iloc[i, j]`**
 - подтаблица **`data.iloc[list of i, list of j]`**
<!-- #endregion -->

<!-- #region id="oPTJKoQJOpb8" -->
`DataFrame` похож на двумерный массив. Как обратиться к его элементам? У `DataFrame` есть колонки (columns) и индексы (index):
- **columns** — это те названия полей, которые вы видите;
- **index** — это идентификатор строки, по умолчанию если ничего не указано то индекс это просто нумерация строк от 1 до n.
<!-- #endregion -->

```python id="Wj0HW6_KOpb9" outputId="8d3ad8a6-1e8f-43ea-ec58-255725c9671b" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675957969067, "user_tz": -180, "elapsed": 370, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.columns
```

```python id="-5Tgi57HOpb9" outputId="ac4a41fa-b4e0-44c6-bcf4-69dbb9f507cc" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675957988154, "user_tz": -180, "elapsed": 377, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.index
```

<!-- #region id="QKrm_SBgOpb-" -->
#### Изменение идекса
<!-- #endregion -->

<!-- #region id="erBpobeFOpb-" -->
Метод `set_index` вернет новый `DataFrame`, с установленным новым индексом.
Если нужно применить изменения к текущему `DataFrame` и не возвращать новый, нужно указать `inplace=True`

 **Важное замечание.**
 Обращайте внимение на то имеет ли тот или иной метод параметр `inplace`. Если такой параметр есть, по умолчанию его значение равно `False` и *возвращается новый объект*, при этом текущий не изменяется, если `inplace=True` возваращается `None` (иначе говоря ничего не возвращается), и изменения применяются к текущему объекту.
<!-- #endregion -->

```python id="dfVpMIeqOpb-"
data.set_index('Runtime', inplace=True)
```

```python id="RywqKuVQOpb_" outputId="1b7204aa-359a-4c25-a8a5-0515b53c11a5" colab={"base_uri": "https://localhost:8080/", "height": 464} executionInfo={"status": "ok", "timestamp": 1675958075891, "user_tz": -180, "elapsed": 405, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.head(3)
```

```python id="zETspElGOpb_" outputId="bc1b23eb-6131-4992-d032-58a17ef8c84c" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958086738, "user_tz": -180, "elapsed": 388, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.index
```

<!-- #region id="rM3ut2rwOpb_" -->
Обновим наш `DataFrame`:
<!-- #endregion -->

```python id="eJW2iOKEOpcA"
data = pd.read_csv("movies.csv", sep=',')
```

```python id="bRBMNKYkOpcA" outputId="02f2ee22-260d-4b5f-fcee-52dc430ba6c3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958110770, "user_tz": -180, "elapsed": 369, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.index
```

<!-- #region id="AZWnGyQyOpcA" -->
Чтобы обратиться к элементу таблицы, пользуясь колонками и индексами, нужно воспользоваться методом `loc[index,column]`. Например, посмотрим, что хранится в первой строчке поля `Stars`:
<!-- #endregion -->

```python id="tabbOVX0OpcA" outputId="39e24332-44df-42a9-b606-776c6fc7aefc" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1675958137732, "user_tz": -180, "elapsed": 377, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[0, 'Stars']
```

<!-- #region id="Ke9NIDyYOpcB" -->
Но бывает удобно обращаться к элементу по его порядковому номеру, тогда нужно использовать `iloc[i, j]`, где нумерация начитается с 0.
<!-- #endregion -->

```python id="oxXDZq8QOpcB" outputId="20571e29-4ead-41b0-bb16-43930a58d4b0" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1675958178106, "user_tz": -180, "elapsed": 533, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.iloc[0, 0]
```

<!-- #region id="T_Pm6MFROpcB" -->
#### Транспонирование
<!-- #endregion -->

<!-- #region id="IRW2ZtuROpcC" -->
Замена столбцов на строки.
<!-- #endregion -->

```python id="yroMFQOAOpcC" outputId="cd8b6d81-9df6-452f-e16e-38292316cc8a" colab={"base_uri": "https://localhost:8080/", "height": 403} executionInfo={"status": "ok", "timestamp": 1675958207986, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.T.head()
```

```python id="EbvzBU_BOpcC" outputId="be7bce82-d8b0-4339-8be6-d0253db41bcd" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958250094, "user_tz": -180, "elapsed": 1012, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
print(data.T.shape)
print(data.T.columns)
```

<!-- #region id="74qyhoNrOpcD" -->
#### pd.Serires
<!-- #endregion -->

<!-- #region id="y6pYy4gNOpcD" -->
Каждая колонка в `DataFrame` — это объект `Series`, у этого объекта тоже есть индексы. Чтобы получить всю колонку `'Title'`, нужно просто указать ее в квадратных скобках.
<!-- #endregion -->

<!-- #region id="7TAEHrsmOpcD" -->
**Замечание**
К колонке можно обращаться через квадратные скобоки или через точку. Предпочтительнее — через квадратные скобки, так как обращение через точку похоже на вызов метода, но обращение через точку быстрее набрать.
<!-- #endregion -->

```python id="Mxmg_DisOpcE" outputId="d11f459e-4658-4e0f-f87e-300ab90c8f46" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958328129, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Title'].head()
```

```python id="1bBhltbpOpcE" outputId="50e1d520-9a57-4747-e240-388c9301bfc3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958332628, "user_tz": -180, "elapsed": 360, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.Title.head()
```

<!-- #region id="Pcdgim8TOpcE" -->
Чтобы получить строку из данных, можно вызвать метод `loc`, указав индекс строки (не НОМЕР).

**Важно:** `loc` — это обращение по индексу, в частном случае индекс и нумерация могут совпадать. **Строка — это тоже `Series`** у которого индексы — это названия столбцов.
<!-- #endregion -->

```python id="W5OJZfwEOpcF" outputId="276ef244-45b6-40e0-ce03-b084c81c3d86" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958396777, "user_tz": -180, "elapsed": 581, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[0]
```

```python id="WmTSX_-UOpcF" outputId="6c2de445-f9fd-4241-ea47-27675a2e1466" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958418873, "user_tz": -180, "elapsed": 537, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
type(data.loc[0])
```

```python id="SLdySlxeOpcF" outputId="dbe73995-de10-49bc-a5be-5b9726dcb676" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1675958431466, "user_tz": -180, "elapsed": 389, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[0]['Title']
```

<!-- #region id="6CLheU-eOpcG" -->
###Поиск и фильтрация
<!-- #endregion -->

<!-- #region id="MXncvXPbOpcG" -->
#### Отбор данных по столбцам
<!-- #endregion -->

<!-- #region id="CSl6QS3kOpcI" -->
Например, нас интересуют не все поля\признаки\столбцы, а только некоторый список полей.
<!-- #endregion -->

```python id="oMFFJheROpcJ"
sub_data = data[['Title', 'Rating']]
```

```python id="ik_6dw98OpcJ" outputId="051ec042-5c04-4075-f727-20ccb12923ca" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675958492178, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
sub_data.head()
```

<!-- #region id="NKoZmL9oOpcJ" -->
#### Отбор данных по строкам
<!-- #endregion -->

<!-- #region id="s8YqJyzvOpcK" -->
Отбор по индексам
<!-- #endregion -->

```python id="eVyl4ZgOOpcK"
sub_data_row = data.loc[[5, 800, 1234]]
```

```python id="r3im4_LfOpcK" outputId="9ca3d101-dab2-485e-888a-4716e1a819d2" colab={"base_uri": "https://localhost:8080/", "height": 381} executionInfo={"status": "ok", "timestamp": 1675958532368, "user_tz": -180, "elapsed": 877, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
sub_data_row
```

<!-- #region id="NvVaCi8AOpcK" -->
#### Отбор по строкам и по столбцам
<!-- #endregion -->

<!-- #region id="4D0-_ESBOpcL" -->
Индексы + названия колонок
<!-- #endregion -->

```python id="ExjNmXQWOpcL" outputId="dea384e9-4a9b-4137-b2f4-f09fc350f929" colab={"base_uri": "https://localhost:8080/", "height": 143} executionInfo={"status": "ok", "timestamp": 1675958577657, "user_tz": -180, "elapsed": 5, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[[5, 800, 1234]][['Title', 'Rating']]
```

<!-- #region id="ZeSVbltxOpcL" -->
2 вариант:
<!-- #endregion -->

```python id="z6G8Id0tOpcM" outputId="94ad3a94-4303-4a16-e231-76a72d123a8d" colab={"base_uri": "https://localhost:8080/", "height": 143} executionInfo={"status": "ok", "timestamp": 1675958597815, "user_tz": -180, "elapsed": 359, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[[5, 800, 1234], ['Title', 'Rating']]
```

```python id="ds57IuK6OpcM" outputId="495c8e0e-bd44-4ac4-9ddc-cf8b75cb037c" colab={"base_uri": "https://localhost:8080/", "height": 237} executionInfo={"status": "ok", "timestamp": 1675958630648, "user_tz": -180, "elapsed": 369, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.loc[:5, 'Title':'Year']
```

<!-- #region id="TXDdCXU_OpcM" -->
По нумерации строк и столбцов:
<!-- #endregion -->

```python id="gOtjTm-YOpcN" outputId="05f0af41-428d-4ebf-e1c8-ed41c2e19a23" colab={"base_uri": "https://localhost:8080/", "height": 143} executionInfo={"status": "ok", "timestamp": 1675958654242, "user_tz": -180, "elapsed": 383, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.iloc[[10, 50, 100], [0, 5]]
```

<!-- #region id="qKnEm6NnOpcN" -->
До 6-й строки (нумерация с 0) и по столбацам с 1 до 4:
<!-- #endregion -->

```python id="JbkN2JkfOpcN" outputId="8d961845-7090-4adf-b771-7694e76d3865" colab={"base_uri": "https://localhost:8080/", "height": 237} executionInfo={"status": "ok", "timestamp": 1675958678641, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.iloc[:6, 1:4]
```

<!-- #region id="k1dPK7BYOpcN" -->
#### Отбор данных по условию
<!-- #endregion -->

```python id="J6tt9hgdOpcO" outputId="51a5fef8-f96e-43ad-db63-c75975820c8a" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958731057, "user_tz": -180, "elapsed": 374, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Month'].unique()
```

<!-- #region id="_utbsJaHOpcO" -->
Отберем данные только по фильмам, вышедшим в декабре.

Общая схема отбора такая: `data[маска]`. Маска — например, `Series` со значениями `True` и `False`.
<!-- #endregion -->

```python id="L1pLWlLKOpcO"
mask = (data['Month'] == 'December')
```

```python id="jWWVc_tJOpcO" outputId="a2edfefd-f53a-4382-8694-a7d2b302506f" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675958784249, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
mask.head()
```

```python id="h_89PrxMOpcP"
data_neutral = data[mask]
```

```python id="N1vzY-uUOpcP" outputId="9675ba2e-84ea-454f-e3f4-931305a6944c" colab={"base_uri": "https://localhost:8080/", "height": 617} executionInfo={"status": "ok", "timestamp": 1675958812862, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data_neutral.head()
```

<!-- #region id="cqN8t1GfOpcP" -->
Можно писать более сложные условия:
<!-- #endregion -->

```python id="pWrmkLxIOpcQ" outputId="5bee6463-564c-4b0f-f37d-2c1af49e8731" colab={"base_uri": "https://localhost:8080/", "height": 600} executionInfo={"status": "ok", "timestamp": 1675958848989, "user_tz": -180, "elapsed": 4, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data[(data['Month'] == 'December') & (data['Rating'] >= 8.0)].head()
```

<!-- #region id="QC7oVcOIOpcQ" -->
#### Фильтрация по индексам и колонкам с помощью метода `filter`
<!-- #endregion -->

<!-- #region id="gUiVrVDqOpcQ" -->
[Документация по filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html)
<!-- #endregion -->

<!-- #region id="MeCxoKA4OpcQ" -->
Отбор по названию колонок:
<!-- #endregion -->

```python id="8FN8CREbOpcR" outputId="74198cb0-63b1-4c75-b8d9-8caf8938e8ba" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675958912893, "user_tz": -180, "elapsed": 362, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.filter(items=['Title', 'Genre']).head()
```

<!-- #region id="LOe1caBPMV__" -->
Отбор колонок, содержащих 'R' в названии:
<!-- #endregion -->

```python id="S3eKIURROpcR" outputId="eee66b07-ef5c-44df-e6af-6c0d113225f9" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675958939948, "user_tz": -180, "elapsed": 375, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.filter(like='R').head()
```

<!-- #region id="my-1LMhqOpcR" -->
**Отбор по регулярному выражению.**

**Регулярные выражения** — это шаблоны, используемые для сопоставления последовательностей символов в строках.

Чтобы отбирать по индексам, нужно указать `axis=0`.
<!-- #endregion -->

<!-- #region id="jEt3_DfHOpcS" -->
Индексы, заканчивающиеся на 10 или содержащие 5:
<!-- #endregion -->

```python id="o3urfZ9sOpcS" outputId="d60b43ec-03f7-4c4b-ec2b-0a17ccab11ff" colab={"base_uri": "https://localhost:8080/", "height": 652} executionInfo={"status": "ok", "timestamp": 1675958997186, "user_tz": -180, "elapsed": 419, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.filter(regex='10$|5', axis=0).head()
```

<!-- #region id="J221u40-OpcV" -->
###Сортировка
<!-- #endregion -->

<!-- #region id="QD0GCixGOpcV" -->
Данные можно сортировать по одному или нескольким столбцам, а также по индексам.
<!-- #endregion -->

<!-- #region id="-yOrwC99OpcV" -->
#### Сортировка по индексу
<!-- #endregion -->

<!-- #region id="W6USlS02OpcV" -->
По умолчанию сортировка всегда осуществляется в порядке возрастания.
<!-- #endregion -->

```python id="KK4eAGtsOpcW" outputId="0198a9c0-09df-4039-8968-c5e566d305a2" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959051695, "user_tz": -180, "elapsed": 625, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sort_index()
```

<!-- #region id="jha8KRzWOpcW" -->
Чтобы изменить порядок сортировки нужно указать `ascending=False`:
<!-- #endregion -->

```python id="Md_Zv3SbOpcW" outputId="0b80d4dd-aa6d-4c47-c8f1-01baf1fc7f92" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959088638, "user_tz": -180, "elapsed": 376, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sort_index(ascending=False)
```

<!-- #region id="8EirypjnOpcX" -->
Сортировка по названию столбцов:
<!-- #endregion -->

```python id="WKVqC9F7OpcX" outputId="01de5b7a-024f-49a9-a220-0fa2311a3088" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959118269, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sort_index(axis=1)
```

<!-- #region id="rZTaOi8YOpcX" -->
#### Сортировка по столбцу
<!-- #endregion -->

```python id="HK4vGJUuOpcY" outputId="a4b2f7fb-595f-421b-dbb3-ebf31787c746" colab={"base_uri": "https://localhost:8080/", "height": 423} executionInfo={"status": "ok", "timestamp": 1675959192910, "user_tz": -180, "elapsed": 417, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sort_values('Year')[['Title', 'Year']].dropna()
```

<!-- #region id="T4ybLS9KOpcY" -->
Далее пример сортировки по столбцам.

Здесь мы используем метод `dropna`, о котором подробнее поговорим позднее.
<!-- #endregion -->

```python id="MzzuAHGyOpcY" outputId="2271a0f5-7028-474c-ba76-2cf21b142376" colab={"base_uri": "https://localhost:8080/", "height": 423} executionInfo={"status": "ok", "timestamp": 1675959357784, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.sort_values(['Year', 'Rating'])[['Title', 'Year', 'Rating']].dropna()
```

<!-- #region id="rCY2T893OpcY" -->
###Переименование
<!-- #endregion -->

<!-- #region id="46t3DKlrOpcZ" -->
[Документация по `rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html)
<!-- #endregion -->

<!-- #region id="xDvFR2HBOpcZ" -->
Переименование столбцов по словарю:
<!-- #endregion -->

```python id="l4SETugfOpcZ" outputId="873a89c6-36f1-4eb3-878b-759140bd64bb" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959539901, "user_tz": -180, "elapsed": 379, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.rename(columns={'Title':'Film title', 'Rating': 'iMDB Score'})
```

<!-- #region id="b9KePA1NOpca" -->
Переведем все колонки в нижний регистр:
<!-- #endregion -->

```python id="soZM_TCDOpca" outputId="c7725fb2-ffb7-42c2-a503-c4f42f7d4230" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959546567, "user_tz": -180, "elapsed": 389, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.rename(columns=str.lower)
```

<!-- #region id="1-usc6b7Opca" -->
Также можно заменять имена столбцов, применяя к названию некоторую функцию:
<!-- #endregion -->

```python id="9lD8aDApOpca" outputId="9866fcaf-7b82-4148-d57f-90019a1e582c" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675959586733, "user_tz": -180, "elapsed": 371, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.rename(columns=lambda col: 'film' + '_' + col.lower())
```

<!-- #region id="yyFQRxnlOpcb" -->
## Часть 2. Работа с пропусками и операции над данными
<!-- #endregion -->

<!-- #region id="019A5nEWOpcb" -->
Снова воспользуемся датасетом [Top 100 popular movies from 2003 to 2022](https://www.kaggle.com/datasets/georgescutelnicu/top-100-popular-movies-from-2003-to-2022-imdb) (iMDB) — содержит данные о 100 самых популярных фильмах каждого года с 2003 по 2022 года.
<!-- #endregion -->

```python id="0xPubDN6Opcb"
data = pd.read_csv("movies.csv", sep=',')
```

<!-- #region id="SVpK-6rwOpcb" -->
###Статистики по признакам
<!-- #endregion -->

<!-- #region id="Iltwmwe5Opcc" -->
#### Расчет частоты события
<!-- #endregion -->

<!-- #region id="1n6Iqg1w8usi" -->
- `.sum()` вектора из нулей и единиц = количество единиц
- `.mean()` вектора из нулей и единиц = доля единиц
<!-- #endregion -->

<!-- #region id="YZ8PBPnFOpcc" -->
Средний рейтинг фильмов:
<!-- #endregion -->

```python id="-NuXXMHtOpcc" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675959868602, "user_tz": -180, "elapsed": 1320, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="c1216b96-d797-43b0-c988-2fcacfe494eb"
data['Rating'].mean()
```

<!-- #region id="nmxEReL4Opcc" -->
Число фильмов по определенным жанрам:
<!-- #endregion -->

```python id="RaWc8WAJOpcd" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675959880080, "user_tz": -180, "elapsed": 851, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="ce7601d3-4e28-43c0-978b-33012f8c3af9"
data['Genre'].value_counts()
```

<!-- #region id="Rc5yYGoBOpcd" -->
Доля фильмов жанра 'Action, Adventure, Sci-Fi':
<!-- #endregion -->

```python id="mMOCIvcOOpcd" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675959913217, "user_tz": -180, "elapsed": 429, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="e8a094b2-2aa8-4bab-d4f1-a92a9b9395c0"
(data['Genre'] == 'Action, Adventure, Sci-Fi').mean()
```

<!-- #region id="PsTNbEnDOpce" -->
Средний рейтинг фильмов в жанре Драма:
<!-- #endregion -->

```python id="wJhCdrL3Opce" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675959943430, "user_tz": -180, "elapsed": 384, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="4605e59e-15dc-4c34-f500-1d767769d7a2"
data[data['Genre'] == 'Drama']['Rating'].mean()
```

<!-- #region id="pL_3VEn4Opce" -->
**Примечание**: метод `count` возвращает число заполненных строк.
<!-- #endregion -->

```python id="z3VFjCw5Opce" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675959974533, "user_tz": -180, "elapsed": 625, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="ad19b816-8db3-441a-a565-4bcde96dcf0a"
data[data['Genre'] == 'Drama']['Rating'].count()
```

<!-- #region id="_op3xx4IOpcf" -->
#### Min, Max, Mean, Median
<!-- #endregion -->

<!-- #region id="e3wy1h-tOpcf" -->
Для числовых признаков можно определить некоторые статистики:
<!-- #endregion -->

```python id="s4KsuJYGOpcf" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960017839, "user_tz": -180, "elapsed": 382, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="d936b091-7a47-4bb9-d4c9-ba9fff5aa348"
data['Rating'].min()
```

```python id="XiupVOQwOpch" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960022228, "user_tz": -180, "elapsed": 394, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="8d6d3f05-dec0-49b8-b04e-5ead20235507"
data['Rating'].max()
```

```python id="s9S8u6MjOpci" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960025234, "user_tz": -180, "elapsed": 616, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="f96d4758-54f0-496d-9bba-6f333d399e62"
data['Rating'].median()
```

```python id="fs9k99EBOpci" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960028871, "user_tz": -180, "elapsed": 374, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="e42d4e72-ec88-44bd-c232-73567f72838e"
data['Rating'].mean()
```

<!-- #region id="cUcHa6RwOpcj" -->
Если нужно оценить сразу все признаки, то:
<!-- #endregion -->

```python id="7U5c7NX9Opcj" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960053044, "user_tz": -180, "elapsed": 988, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="b41e75ba-fdfb-49e2-b837-a90b13661d9d"
data.min()
```

```python id="bAs5MYlqOpcj" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960080819, "user_tz": -180, "elapsed": 388, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="42d19be7-aee6-4abe-b42e-5d19526afea6"
data.max()
```

```python id="11m8ViXSOpck" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960089238, "user_tz": -180, "elapsed": 389, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="34ad1ac4-1941-4842-b57d-461520400306"
data.median()
```

```python id="Hlpz4cbnOpck" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960100405, "user_tz": -180, "elapsed": 362, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}} outputId="6806304b-2a45-445f-a3da-4ccc3310a9b5"
data.mean()
```

<!-- #region id="Fxl8iQnROpcl" -->
###Работа с пропусками
<!-- #endregion -->

<!-- #region id="QGt8MXJdOpcl" -->
Для начала стоит оценить долю пропусков по столбцам и по строкам.

Может оказаться так, что по некоторым столбцам совсем нет данных и там очень много `NULL`-ов, возможно, такие столбцы стоит отбросить. То же самое касается и строк, возможно, по каким-то объектам крайне мало заполненых признаков, и их стоит также отбросить.
<!-- #endregion -->

<!-- #region id="FbwAZ60DOpcl" -->
Посмотрим количество пропусков по признакам:
<!-- #endregion -->

```python id="wgE1MOV5Opcm" outputId="b96ed9d6-2b71-4278-deab-26b2328d5d65" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960174429, "user_tz": -180, "elapsed": 381, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.isnull().sum()
```

<!-- #region id="ty7BAcg4Opcm" -->
Обычно количество незаполненных данных нам мало что говорит, полезнее знать, какая это доля данных.
<!-- #endregion -->

```python id="7nbwAB_zOpcn" outputId="c003c273-d318-4686-afde-876fe32ed1de" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960231580, "user_tz": -180, "elapsed": 455, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.isnull().mean().sort_values(ascending=False)
```

<!-- #region id="6yUEkC5aOpcn" -->
Итак у нас есть 2 признака с пропусками Certificate и Rating.
<!-- #endregion -->

<!-- #region id="tm8VKUAfOpcn" -->
#### Отбрасывание пропусков
<!-- #endregion -->

<!-- #region id="aKUUI1AFOpco" -->
Например, вы решили отбросить данные с пропусками, как это сделать?
С помощью метода [`dropna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html). Обратите внимание, что у этого метода есть параметр `inplace`.
<!-- #endregion -->

```python id="nOffBpgXOpco" outputId="5e6b6a7a-4bee-46fc-befc-816034bbad96" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960297558, "user_tz": -180, "elapsed": 368, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.dropna(subset=['Certificate', 'Rating']).isnull().mean()
```

<!-- #region id="C9A3mh21Opco" -->
#### Заполнение пропусков значением
<!-- #endregion -->

<!-- #region id="LB4LwoeLOpco" -->
Заполнять пропуски можно с помощью метода [`fillna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)
<!-- #endregion -->

<!-- #region id="X-0VAVcfOpcp" -->
Чем можно заполнить пропуски?
<!-- #endregion -->

```python id="RQUne-QCOpcp" outputId="d04bf514-39e0-4e23-d150-28a73abafb13" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960336570, "user_tz": -180, "elapsed": 382, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating'].fillna(value=100)
```

```python id="yhs8gu47Opcp" outputId="e903099f-a7bb-4a2c-af61-795c5ffcd1e4" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960356421, "user_tz": -180, "elapsed": 391, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating'].fillna(value=0)
```

<!-- #region id="Ja-84-a5Opcp" -->
Можно заполнить средним или медианой:
<!-- #endregion -->

```python id="sjdNGJ8ROpcq" outputId="aaa8e5d6-25d9-4bea-a2c6-6d166c2aa59b" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960392457, "user_tz": -180, "elapsed": 359, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating'].fillna(value=data['Rating'].median())
```

<!-- #region id="Ib269OTCOpcq" -->
Пропуски можно заполнять также с помощью последнего непропещунного значения в прямом (ffill) и обратном (bfill) порядках.
<!-- #endregion -->

```python id="m8rKMzJvOpcq" outputId="9c484b5a-5973-421e-8f76-f5dfa04a0b9a" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960424840, "user_tz": -180, "elapsed": 370, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating'].fillna(method='ffill')
```

<!-- #region id="qaCG7O1iOpcq" -->
#### Удаление дубликатов
<!-- #endregion -->

<!-- #region id="z1y1GScBOpcr" -->
Бывает, что в данных есть дубликаты. Если так получилось, то для начала стоит подумать, почему они появились: нет ли в ошибок в получении таких данных. Если же дубликаты есть, то удалить их просто с помощью метода [`drop_duplicates`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html).
<!-- #endregion -->

```python id="qMpviet1Opcr"
data.drop_duplicates(inplace=True)
```

<!-- #region id="sH4ay8VYOpcr" -->
###Применение функции к данным, расчет новых значений
<!-- #endregion -->

<!-- #region id="RVfVO3MPOpcs" -->
Предположим, мы хотим создать новый признак, который будет делить фильмы на 3 категории в зависимости от их рейтинга. Как это сделать?
<!-- #endregion -->

<!-- #region id="Z6pPIXKTOpcs" -->
#### Apply
<!-- #endregion -->

<!-- #region id="RwQ5rfzbOpcs" -->
Напишем функцию, которая по рейтингу определяет категорию:
<!-- #endregion -->

```python id="IVEPbZJCOpcs" outputId="8ec97c1c-cc85-4b9d-8322-ea2b10b6832e" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960550127, "user_tz": -180, "elapsed": 368, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating'].unique()
```

```python id="I2wmt6aAOpcs"
def rating_group(rating):
    if rating >= 8:
        return 'Good'
    if rating <= 6:
        return 'Bad'
    else:
        return 'Medium'
```

<!-- #region id="UqjWVYq3Opcv" -->
А теперь применяем функцию к данным с помощью метода `apply`:
<!-- #endregion -->

```python id="XC2I6SvhOpcv"
data['Rating_group'] = data['Rating'].apply(rating_group)
```

<!-- #region id="1SRBiWG1Opcv" -->
В данном случае мы воспользовались методом `Series`, но такой же метод есть и у `DataFrame`.
<!-- #endregion -->

```python id="0W0RiQxlOpcv" outputId="e3ee5543-a5df-4abd-b15a-83302829d3f4" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960624834, "user_tz": -180, "elapsed": 395, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Rating_group'].head()
```

<!-- #region id="lMc7B1yaOpcw" -->
Теперь нам нужно сформировать новый признак, который использует информацию сразу о нескольких признаках. Применим метод `apply` ко всему `DataFrame`.
<!-- #endregion -->

<!-- #region id="wX4ETwFKOpcw" -->
Все фильмы с высокой оценкой и жанром драма выделим в отдельную группу:
<!-- #endregion -->

```python id="ozCH3XHMOpcw"
data['New_feature'] = data.apply(lambda row:
                                       1 if 7.5 < row['Rating'] < 10.0 and row['Genre'] == 'Drama'
                                        else 0, axis=1)
```

```python id="s96PH8ZfOpcw" outputId="e32bb35f-3ad2-4bd0-f993-c2b7f8f0c6c6" colab={"base_uri": "https://localhost:8080/", "height": 369} executionInfo={"status": "ok", "timestamp": 1675960688831, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data[data['New_feature'] == 1].head()
```

<!-- #region id="6EA5hykFOpcx" -->
#### Пример работы со строками
<!-- #endregion -->

<!-- #region id="QkiC1frLOpcx" -->
Подробнее в [документации](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html).
<!-- #endregion -->

```python id="qgpTKamUOpcx" outputId="a54731ae-b2df-4fb4-a3b1-da8e62ea53ae" colab={"base_uri": "https://localhost:8080/", "height": 423} executionInfo={"status": "ok", "timestamp": 1675960764588, "user_tz": -180, "elapsed": 528, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Stars'].str.split(', ', n=3, expand=True)
```

```python id="PvyRcXVSOpcy" outputId="61972e5a-5853-47ec-f8d5-db3f1edd90a2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960788807, "user_tz": -180, "elapsed": 357, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Stars'].str.len()
```

```python id="fx3IjM5WOpcy" outputId="e788d36e-f168-4629-f99f-2f517439dffb" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675960820084, "user_tz": -180, "elapsed": 390, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data['Stars'].str.contains('Brad Pitt')
```

<!-- #region id="qtZrCY5_Opcy" -->
#### Map
<!-- #endregion -->

<!-- #region id="imzSY--8Opcz" -->
Заметим, что в данных есть бинарный признак `Rating_group`, который можно закодировать с помощью 0 и 1 вот так:
<!-- #endregion -->

```python id="fdF-ieZXOpcz"
data['Rating_group_new'] = data['Rating_group'].map({'Good': 0, 'Medium': 1})
```

```python id="UJr3nd3hOpc0" outputId="09949df6-a3b6-4974-f9c5-04d5003f9961" colab={"base_uri": "https://localhost:8080/", "height": 438} executionInfo={"status": "ok", "timestamp": 1675960910982, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.head()
```

<!-- #region id="Sw2NcF2lOpc0" -->
Для дальнейшего изложения, удалим вновь созданные признаки:
<!-- #endregion -->

```python id="YJ15FFIeOpc0"
data.drop(['Rating_group', 'New_feature', 'Rating_group_new'], inplace=True, axis=1)
```

<!-- #region id="c5q39e0ZOpc1" -->
###Группировка и агрегация с GroupBy
<!-- #endregion -->

<!-- #region id="3exrKlKzOpc1" -->
[**Split -> Apply -> Combine**](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
<!-- #endregion -->

<!-- #region id="D6PpBIRzOpc1" -->
Под «группировкой» мы подразумеваем процесс, включающий один или несколько из следующих шагов:
- **Splitting the data** (разбиение на группы);
- **Applying a function** (применение функции к каждой группе);
- **Combining the results** (объединение результата).
<!-- #endregion -->

<!-- #region id="C_u7WPwzOpc1" -->
Как посчитать среднюю оценку фильмов в каждом месяце?
<!-- #endregion -->

```python id="1m5-Jk-jOpc1" outputId="f49e3a5e-fda6-4627-ab8b-65e743ceafad" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675961015902, "user_tz": -180, "elapsed": 390, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
data.groupby('Month')['Rating'].mean()
```

<!-- #region id="ijGRDVcfOpc2" -->
Аналогично `GROUP BY` в SQL:
```sql
    SELECT
        Month,
        AVG(Rating)
    FROM data
    GROUP BY
        Month;
```
<!-- #endregion -->

<!-- #region id="HQEj57idOpc2" -->
#### Разбиение (Split)
<!-- #endregion -->

<!-- #region id="2ySYHGjrOpc2" -->
##### Разбиение по одному признаку
<!-- #endregion -->

<!-- #region id="CdIRlo6LOpc2" -->

`GroupBy` хранит исходный `DataFrame` (или `Series`) и разбиение на группы, т.е. соответствие «название группы (значение колонки, по которой группируем) — список индексов»:
<!-- #endregion -->

```python id="F3JAEXT_Opc3" outputId="b3c7d5a4-ae34-4c58-e158-9657ae711ada" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675961163143, "user_tz": -180, "elapsed": 1190, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
splits = data.groupby('Genre')
print(type(splits))
```

```python id="5vPFHdN3Opc3" outputId="2f0c4f7b-7276-4e09-cb1d-e2475945e30d" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1675961174591, "user_tz": -180, "elapsed": 414, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
splits.groups
```

<!-- #region id="S2K-P7oeOpc3" -->
**get_group**
<!-- #endregion -->

```python id="OwKSndh5Opc3" outputId="22ea465a-196f-4a21-8cfb-cf6757522136" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1675961210937, "user_tz": -180, "elapsed": 379, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
splits.get_group('Drama')  # тот же результат, что и data.loc[data.Genre == 'Drama']
```

<!-- #region id="doFCedZwOpc4" -->
##### agg
<!-- #endregion -->

<!-- #region id="Pyo3EqBDOpc4" -->
Применение нескольких функций.

[Документация по `agg`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)
<!-- #endregion -->

```python id="_19qky9oOpc4" outputId="a1b5ae6a-4a2e-4070-b2f7-1cf0f8d40f06" colab={"base_uri": "https://localhost:8080/", "height": 455} executionInfo={"status": "ok", "timestamp": 1675961261718, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
splits['Rating'].agg(['mean', 'std', 'count'])
```

<!-- #region id="Og4LruzLOpc4" -->
## Часть 3. Работа с несколькими таблицами (Join)
<!-- #endregion -->

<!-- #region id="xPEHUnQdOpc5" -->
### Соединение таблиц в `Pandas`
`Merge`, `join` и `concatenate`
<!-- #endregion -->

<!-- #region id="4GBUV9BrOpc7" -->
Соединения двух или более таблиц данных по совпадающему условию.
Подробнее в [документации](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html).
<!-- #endregion -->

<!-- #region id="lTVelZiPOpc7" -->
Создадим 3 таблицы для демонстрации:
<!-- #endregion -->

<!-- #region id="MrfVF5CiOpc7" -->
#### Первая таблица
<!-- #endregion -->

```python id="kTgPffaEOpc8" outputId="6ccd889f-b928-4414-ab8b-5de2e84a74c4" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675961403333, "user_tz": -180, "elapsed": 366, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
raw_data = {
        'user_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Jin', 'Alex', 'Shelly', 'Anna', 'Troy'],
        'last_name': ['Kazama', 'Lewis', 'Tenant', 'Ivanova', 'Brown']}
df_a = pd.DataFrame(raw_data, columns = ['user_id', 'first_name', 'last_name'])
df_a
```

<!-- #region id="gDEu3tM-Opc8" -->
#### Вторая таблица
<!-- #endregion -->

```python id="CBoZ7BQbOpc8" outputId="be9d6d9d-48e6-416c-897b-892d134c8993" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675961424984, "user_tz": -180, "elapsed": 3, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
raw_data = {
        'user_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Anna', 'Troy', 'Rio', 'Terry', 'Peter'],
        'last_name': ['Ivanova', 'Brown', 'Ferdinand', 'Parker', 'Parker']}
df_b = pd.DataFrame(raw_data, columns = ['user_id', 'first_name', 'last_name'])
df_b
```

<!-- #region id="JESJkb9HOpc8" -->
#### Третья таблица
<!-- #endregion -->

```python id="5NE01OaTOpc9" outputId="b83a91ac-515f-40fa-f7a9-bc5d6567ceed" colab={"base_uri": "https://localhost:8080/", "height": 331} executionInfo={"status": "ok", "timestamp": 1675961450056, "user_tz": -180, "elapsed": 552, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
raw_data = {
        'user_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10'],
        'outer_id': [223, 1134, 89, 671, 278, 17, 1931, 216, 81]}
df_c = pd.DataFrame(raw_data, columns = ['user_id','outer_id'])
df_c
```

<!-- #region id="Y7QHgD3qOpc9" -->
### Конкатенация по строкам
<!-- #endregion -->

```python id="dDeOTfskOpc9" outputId="886abcaf-07de-4821-8b8b-d6963504637a" colab={"base_uri": "https://localhost:8080/", "height": 363} executionInfo={"status": "ok", "timestamp": 1675961472679, "user_tz": -180, "elapsed": 378, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
df_new = pd.concat([df_a, df_b], ignore_index=True)
df_new
```

<!-- #region id="4lK7sAuPOpc-" -->
### Конкатенация по столбцам
<!-- #endregion -->

```python id="XhWuQJETOpc-" outputId="fb51b5b1-1232-4d60-a556-559fc4bfcdad" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675961510464, "user_tz": -180, "elapsed": 391, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.concat([df_a, df_b], axis=1)
```

<!-- #region id="mM2sZKAOOpc-" -->
### Merge таблиц по `user_id`
<!-- #endregion -->

```python id="xgeNhYqsOpc-" outputId="629dfb11-ae17-4e6c-a3b8-d70e7d874df7" colab={"base_uri": "https://localhost:8080/", "height": 331} executionInfo={"status": "ok", "timestamp": 1675961610130, "user_tz": -180, "elapsed": 372, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_new, df_c, on='user_id')
```

<!-- #region id="9taN2BQUOpc_" -->
### Merge таблиц по `user_id` в левой таблице и `user_id` в правой
<!-- #endregion -->

```python id="Z6QWpJBxOpc_" outputId="b0f80a0c-e2eb-4edd-d3f4-fc37a08b8a6d" colab={"base_uri": "https://localhost:8080/", "height": 331} executionInfo={"status": "ok", "timestamp": 1675961696932, "user_tz": -180, "elapsed": 1100, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_new, df_c, left_on='user_id', right_on='user_id')
```

<!-- #region id="_ccpU9uTOpdA" -->
### Outer join
<!-- #endregion -->

```python id="56t7qo9COpdA" outputId="56f50f2f-f5c1-4e1e-dbac-3d60b4fb2226" colab={"base_uri": "https://localhost:8080/", "height": 300} executionInfo={"status": "ok", "timestamp": 1675961729437, "user_tz": -180, "elapsed": 403, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_a, df_b, on='user_id', how='outer')
```

<!-- #region id="HjoQjjJTOpdA" -->
### Inner join
<!-- #endregion -->

```python id="FSBKEqxCOpdA" outputId="a07977b5-598c-4964-f70c-e47450c898bb" colab={"base_uri": "https://localhost:8080/", "height": 112} executionInfo={"status": "ok", "timestamp": 1675961759514, "user_tz": -180, "elapsed": 375, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_a, df_b, on='user_id', how='inner')
```

<!-- #region id="L6ptgtYEOpdB" -->
### Left/Right join
<!-- #endregion -->

```python id="9cs-4on4OpdB" outputId="9d9e7c6f-12f5-4777-b820-ff8c5572e09b" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675961776490, "user_tz": -180, "elapsed": 394, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_a, df_b, on='user_id', how='left')
```

```python id="uVlkREsdOpdB" outputId="b99c4f56-d73b-4290-9417-f6e92cca1bd2" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1675961794361, "user_tz": -180, "elapsed": 721, "user": {"displayName": "\u0420\u043e\u043c\u0430\u043d \u041c\u0430\u043b\u044b\u0448\u0435\u0432", "userId": "03259385954991268430"}}
pd.merge(df_a, df_b, on='user_id', how='right')
```
