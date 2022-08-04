#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/7/24
# 1.2 解压可迭代对象赋值给多个变量.py

# 如果一个可迭代对象的元素个数超过变量个数时，会出现”太多解压值”的异常。那么怎样才能从这个可迭代对象中解压出N个元素出来？
from audioop import avg


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

    #
    # def sum(sales_record):
    #     *trailing_qtrs, current_qtr = sales_record
    #     trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    #     return avg_comparison(trailing_avg, current_qtr)


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


if __name__ == '__main__':
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name)
    print(email)
    print(phone_numbers)

    # 星号表达式也能用在列表的开始部分。比如，你有一个公司前8个月销售数据的序列，
    # 但是你想看下最近一个月数据和前面7个月的平均值的对比。你可以这样做：
    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing)
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    # 字符串分割
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')

    print(uname)
    print(fields)
