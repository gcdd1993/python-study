#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.6 字典中的键映射多个值.py

# 怎样实现一个键对应多个值的字典（也叫 multidict）？
# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
# 就需要将这多个值放到另外的容器中，比如列表或者集合里面
from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    print(d)
