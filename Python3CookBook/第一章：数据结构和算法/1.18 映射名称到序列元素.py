#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.18 映射名称到序列元素.py
# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读，于是你想通过名称来访问元素。
from collections import namedtuple

if __name__ == '__main__':
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub.addr)
    print(sub.joined)
