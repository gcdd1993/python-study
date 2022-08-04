#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.19 转换并同时计算数据.py

# 你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ），但是首先你需要先转换或者过滤数据

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)
    print(s)


