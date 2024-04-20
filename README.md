# Изображение проекции полиэдра

Построение изображения полиэдра с удалением невидимых линий — пример
классической задачи, для успешного решения которой необходимо знакомство
с основами вычислительной геометрии.

![Шахматный король](images/king.png)

## Модификация проекта

### Постановка задачи

> Назовём точку в пространстве «хорошей», если её проекция находится строго внутри окружности `x^2+y^2 = 4`, но строго 
> вне окружности `x^2+y^2 = 1`.
> Модифицируйте эталонный проект таким образом, чтобы определялась и печаталась следующая характеристика полиэдра: сумма
> длин рёбер, оба из концов которых — «хорошие» точки.

### Последовательность решения задачи

1. В класс tkdrawer добавляется метод для рисования кольца.
2. Координаты точек, необходимых для рисования кольца, умножаются на коэффициент гомотетии для корректного отображения.
3. В класс R3 добавляется метод, проверяющий, является ли конкретная точка хорошей.
4. В класс Edge добавляется метод, вычисляющий длину ребра.
5. При построении полиэдра в классе Polyedr теперь вычисляется суммарный периметр ребер, оканчивающихся «хорошими»
точками.
6. Создается массив смежности вершин, необходимый для отбрасывания ситуаций, в которых одно ребро принадлежит
двум граням и может быть случайно посчитано дважды.
7. Добавлены соответствующие тесты на проверку правильности вычисления периметра полиэдра.
## Проверка соблюдения соглашений о стиле программного кода

~~~{.sh}
find . -name '*.py' -exec pycodestyle {} \;
~~~

## Проверка покрытия тестами кода программы

~~~{.sh}
python -B -m coverage run -m unittest discover tests && coverage report -m ; rm -f .coverage
~~~
