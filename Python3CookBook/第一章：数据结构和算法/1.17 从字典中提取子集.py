#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.17 从字典中提取子集.py
# 你想构造一个字典，它是另外一个字典的子集。

if __name__ == '__main__':
    # 最简单的方式是使用字典推导
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}

    print(p1)
    print(p2)
