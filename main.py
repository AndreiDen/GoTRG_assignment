import math


def get_boxes_count(products_count, box_capacity):
    for x in (products_count, box_capacity):
        assert_int(x)
    try:
        boxes = math.ceil(products_count/box_capacity)
        return boxes
    except ZeroDivisionError:
        raise Exception('division by zero')


def assert_int(var):
    if isinstance(var, bool):
        raise Exception('passed argument is boolean')
    elif not isinstance(var, int):
        raise Exception('passed argument is not integer')
    elif var < 0:
        raise Exception('passed argument cannot be negative')
    elif var > 2**1074:
        raise Exception('argument value is too big')



