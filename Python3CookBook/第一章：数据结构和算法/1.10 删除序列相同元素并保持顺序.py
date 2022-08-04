#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.10 删除序列相同元素并保持顺序.py
# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

def dedupe(items):
    """
    如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题

    :param items:
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_map(items, key=None):
    """
    如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题

    :param items:
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_map(a, key=lambda d: (d['x'], d['y']))))

    print(list(dedupe_map(a, key=lambda d: d['x'])))
