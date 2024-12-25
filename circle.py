import math

pi = math.acos(-1)

def area(r):
    '''
    Возвращает площадь круга с радиусом r
    Параметр:
        a (float): радиус круга
    Возвращаемое значение:
        area(float): площадь круга
    Пример вызова:
        area(10) -> 314.1592653589793238462643383
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с радиусом r
    Параметр:
        a (float): радиус круга
    Возвращаемое значение:
        perimeter(float): периметр круга
    Пример вызова:
        perimeter(50) -> 314.1592653589793238462643383
    '''
    return 2 * math.pi * r

