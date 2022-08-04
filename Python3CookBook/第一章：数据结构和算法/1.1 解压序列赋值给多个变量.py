#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/7/24
# 解压序列赋值给多个变量
# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？

if __name__ == '__main__':
    p = (4, 5)
    x, y = p
    print(f"x = {x}, y = {y}")

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)

    name, shares, price, (year, mon, day) = data
    print(year, mon, day)

    # 如果变量个数和序列元素的个数不匹配，会产生一个异常。
    # x, y, z = p

    # 有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况Python并没有提供特殊的语法。
    # 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
    _, shares, price, _ = data
    print(shares, price)
