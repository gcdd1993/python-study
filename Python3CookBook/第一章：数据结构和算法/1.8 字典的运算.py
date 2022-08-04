#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.8 字典的运算.py
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。比
    # 如，下面是查找最小和最大股票价格和股票值的代码：
    min_price = min(zip(prices.values(), prices.keys()))
    # min_price is (10.75, 'FB')
    max_price = max(zip(prices.values(), prices.keys()))
    # max_price is (612.78, 'AAPL')
    print(min_price, max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    # 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。
    # 比如，下面的代码就会产生错误：
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))  # OK
    print(max(prices_and_names))  # ValueError: max() arg is an empty sequence
