#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.16 过滤序列元素.py

if __name__ == '__main__':
    # 最简单的过滤序列元素的方法就是使用列表推导
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])
    print([n for n in mylist if n < 0])
