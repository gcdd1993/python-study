#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.13 通过某个关键字排序一个字典列表.py
# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
from operator import itemgetter

if __name__ == '__main__':
    # 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    # 根据任意的字典字段来排序输入结果行是很容易实现的，代码示例：
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)

    # itemgetter() 函数也支持多个 keys，比如下面的代码
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)

    # itemgetter() 有时候也可以用 lambda 表达式代替，比如：
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
