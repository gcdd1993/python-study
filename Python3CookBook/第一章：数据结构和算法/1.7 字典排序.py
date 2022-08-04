#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.7 字典排序.py
# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
# 一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。


from collections import OrderedDict
import json

if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])

    print(json.dumps(d))
