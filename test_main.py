from main import get_boxes_count
import pytest

@pytest.mark.parametrize(
    'products_count, box_capacity, expected_boxes', [
    (1, 1, 1),
    (2, 1, 2),
    (14, 5, 3),
    (15, 5, 3),
    (16, 5, 4),
    (1, 2, 1),
    (0, 1, 0),
    (1, 2 ** 1074, 1),
    (1, 10 ** 323, 1),
    ])
def test_get_boxes_count_function_positive(products_count, box_capacity, expected_boxes):
    boxes = get_boxes_count(products_count, box_capacity)
    assert boxes == expected_boxes


@pytest.mark.parametrize(
    'products_count, box_capacity, expected_error', [
        (1, 0, 'division by zero'),
        (True, 1, 'passed argument is boolean'),
        (1, False, 'passed argument is boolean'),
        (1, -1, 'passed argument cannot be negative'),
        (-1, 1, 'passed argument cannot be negative'),
        (-1, -1, 'passed argument cannot be negative'),
        (1, 1.1, 'passed argument is not integer'),
        (-1.1, 1, 'passed argument is not integer'),
        (0.1, 0.1, 'passed argument is not integer'),
        ('`', 1, 'passed argument is not integer'),
        ('five', 1, 'passed argument is not integer'),
        (1, [], 'passed argument is not integer'),
        ((1, 2), 1, 'passed argument is not integer'),
        (int, 1, 'passed argument is not integer'),
        (1, (2 ** 1074)+1, 'argument value is too big'),
        (1, 10 ** 324, 'argument value is too big'),
    ])
def test_get_boxes_count_function_negative(products_count, box_capacity, expected_error):
    with pytest.raises(Exception, match=expected_error):
        get_boxes_count(products_count, box_capacity)
