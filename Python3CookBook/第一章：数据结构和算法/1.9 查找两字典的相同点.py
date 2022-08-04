#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.9 查找两字典的相同点.py
# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    # 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作。比如：
    # Find keys in common
    a.keys() & b.keys()  # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys()  # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items()  # { ('y', 2) }

    # 这些操作也可以用于修改或者过滤字典元素。比如，假如你想以现有字典构造一个
    # 排除几个指定键的新字典。下面利用字典推导来实现这样的需求：
    # Make a new dictionary with certain keys removed
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    # c is {'x': 1, 'y': 2}
    print(c)
