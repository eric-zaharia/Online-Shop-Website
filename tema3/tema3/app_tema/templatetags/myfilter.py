import math

from django import template

register = template.Library()


def even(value):
    value = int(value)
    count = 0
    while value != 0:
        i = value % 10
        if i % 2 == 0:
            count += 1
        value /= 10
        value = math.floor(value)
    return count


register.filter('even_no_count', even)
