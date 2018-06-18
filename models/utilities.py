# -*- coding: utf-8 -*-
from math import log10, floor


def num_to_shorthand(num, ends=None):
    """
    Converts Number to short human readable numbers 
    """
    if ends is None:
        ends = ["", "K", "M", "B", "T"]

    num = int(num)
    str_num = str(num)

    index = 0 if not num else int(floor(log10(abs(num))) / 3)

    letter = ends[index]

    digit = str_num[0:len(str_num) - index * 3]

    return '{}{}'.format(digit, letter)


def choices_tuple(choices, is_sorted=True):
    choices = [(i.lower(), i.upper()) for i in choices]

    if is_sorted:
        return sorted(choices, key=lambda tup: tup[0])

    return choices


def odoo_to_pandas_list(orm_query=None, columns=list()):
    """
    Convert odoo query to list if dictionary readabloe to pandas   
    """
    columns = columns if columns else orm_query.fields_get_keys()
    data = []
    for row in orm_query:
        row_data = {}
        for column in columns:
            row_data[column] = row.mapped(column)[0]
        data.append(row_data)
    return data


def int_to_roman(var):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(var, int):
        raise TypeError("expected integer, got %s" % type(var))
    if not 0 < var < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(var / ints[i])
        result.append(nums[i] * count)
        var -= ints[i] * count
    return ''.join(result)
