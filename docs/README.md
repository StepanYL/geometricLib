# Geometric lib
Библиотека, содержащая методы для нахождения периметра и площади геометрических фигур
## Описание функций
###  ${\color {magenta} \textbf{area()}  }$ 
Используется для нахождения площади фигур
<details>
<summary>${\color {cyan} Площадь \ прямоугольника\ - \ area(a, b) \ в \ файле \ rectangle.py}$ </summary>
Функция использует формулу для нахождения площади прямоугольника по двум сторонам: S = ab

Параметры:
  - a (float): длина прямоугольника
  - b (float): ширина прямоугольника

Возвращаемое значение:
  - area (float): площадь прямоугольника

Пример вызова: area(3, 5) -> 15
</details>

<details>
<summary>${\color {cyan} Площадь \ квадрата\ - \ area(a)\ в\ файле\ square.py}$ </summary>

Функция использует формулу для нахождения площади квадрата по длине его стороны: S = a * a

Параметр:
  - a (float): сторона квадрата

Возвращаемое значение:
  - area (float): площадь квадрата

Пример вызова: area(2) -> 4

</details>


<details>
  <summary>${\color {cyan} Площадь \ треугольника\ -\ area(a, h)\ в\ файле\ triangle.py }$ </summary>
Функция использует формулу площади треугольника по длине одной из его сторон и проведенной к этой стороне высоты: S = ah / 2

Параметры:
  - a (float): сторона треугольника
  - h (float): длина перпендикулярной ей высоты

Возвращаемое значение:
  - area (float): площадь треугольника

Пример вызова: area(2.5, 4) -> 5
</details>
<details>
 <summary>${\color {cyan} Площадь \ круга\ -\ area(r)\ в\ файле\ circle.py}$ </summary>
Функция использует формулу площади круга по его радиусу: S = $\pi$ * (r ^ 2).

Параметр:
  - r (float): радиус круга

Возвращаемое значение:
  - area (float): площадь круга

Пример вызова: area(1) -> 3.141592653589793238462643383
</details>

### ${\color {magenta} \textbf{perimeter()}}$
Используется для нахождения периметра фигур

<details>

<summary>${\color {cyan} Периметр \  прямоугольника\ -\ perimeter(a, b)\ в\ файле\ rectangle.py }$</summary>
Функция использует формулу для нахождения периметра прямоугольника по длине двух его сторон: P = (a + b) * 2
Параметры:
  - a (float): длина прямоугольника
  - b (float): ширина прямоугольника

Возвращаемое значение:
  - perimeter (float): периметр прямоугольника

Пример вызова: perimeter(2.5, 3.5) -> 12
</details>

<details>
<summary>${\color {cyan} Периметр \ квадрата\ -\ perimeter(a)\ в\ файле\ square.py}$ </summary>

Функция использует формулу для нахождения периметра квадрата по длине его стороны: P = 4a

Параметр:
  - a (float): сторона квадрата

Возвращаемое значение:
  - perimeter (float): периметр квадрата

Пример вызова: perimeter(25) -> 100

</details>


<details>
  <summary>${\color {cyan} Периметр \  треугольника\ -\ perimeter(a, b, c)\ в\ файле\ triangle.py }$ </summary>
Функция использует формулу для нахождения периметра треугольника по трем его сторонам: S = a + b + c

Параметры:
  - a (float): длина первой  стороны треугольника
  - b (float): длина второй  стороны треугольника
  - c (float): длина третьей стороны треугольника

Возвращает целое число:
  - perimeter (int): периметр треугольника

Пример вызова: perimeter(3, 4, 5) -> 15
</details>
<details> 
  <summary> ${\color {cyan} Периметр \ круга\ -\ perimeter(r)\ в\ файле\ circle.py }$ </summary>
Функция использует формулу для нахождения периметра круга по его радиусу: S = 2 * $\pi$ * r.

Параметр:
  - r (float): радиус круга

Возвращаемое значение:
  - perimeter (float): периметр круга

Пример вызова: area(4) -> 25.132741228718345
</details>

## Описание тестов
<details>
<summary>${\color {cyan} testPerimeterZero}$ </summary>
Тест проверяет случай нулевого периметра
Пример:
check = square.testPerimeterZero(0)
self.assertEqual(check, 0)
</details>

<details>
<summary>${\color {cyan} testPerimeterBigValues}$ </summary>
Тест проверяет корректность нахождения периметра при больших размерах фигуры
Пример:
check = rectangle.perimeter(4611686018427387904, 4611686018427387904)
self.assertEqual(check, 18446744073709551616)
</details>

<details>
<summary>${\color {cyan} testPerimeterPrecision}$ </summary>
Тест проверяет корректность нахождения периметра при необходимой точности eps = 1е-9
Пример:
check1 = rectangle.perimeter(3, 3)
check2 = rectangle.perimeter(3, 3 + eps)
self.assertNotEqual(check1, check2)
</details>

<details>
<summary>${\color {cyan} testAreaZero}$ </summary>
Тест проверяет случай нулевой площади
Пример:
check = square.testAreaZero(0)
self.assertEqual(check, 0)
</details>

<details>
<summary>${\color {cyan} testAreaBigValues}$ </summary>
Тест проверяет корректность нахождения площади при больших размерах фигуры
Пример:
check = circle.area(10000000000)
self.assertEqual(check, 100000000000000000000 * pi)
</details>

<details>
<summary>${\color {cyan} testAreaPrecision}$ </summary>
Тест проверяет корректность нахождения площади при необходимой точности eps = 1e-9
Пример:
check1 = rectangle.area(2, 2)
check2 = rectangle.area(2 + eps, 2)
self.assertNotEqual(check1, check2)
</details>

## Последние изменения:
* 9ee8ef5 - Добавлены тесты и описания к ним
* b2d6e8e - Обновление README.md
* 307a215 - Дубликат README.md удален
* 683f34b - Добавлена документация
* b93e163 - Добавлены описания к функциям в файлах