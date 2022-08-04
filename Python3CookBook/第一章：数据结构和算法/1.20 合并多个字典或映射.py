#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.20 合并多个字典或映射.py

# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在。

if __name__ == '__main__':
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    from collections import ChainMap

    c = ChainMap(a, b)
    print(c['x'])  # Outputs 1 (from a)
    print(c['y'])  # Outputs 2 (from b)
    print(c['z'])  # Outputs 3 (from a)
