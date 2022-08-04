#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.11 命名切片.py

if __name__ == '__main__':
    # 0123456789012345678901234567890123456789012345678901234567890'
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    # 与其那样写，为什么不想这样命名切片呢：
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    # 避免了大量无法理解的硬编码下标，使得你的代码更加清晰可读
    cost = int(record[SHARES]) * float(record[PRICE])
