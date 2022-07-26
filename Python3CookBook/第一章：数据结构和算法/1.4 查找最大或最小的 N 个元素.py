#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.4 查找最大或最小的 N 个元素.py
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题

import heapq

if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

    # 两个函数都能接受一个关键字参数，用于更复杂的数据结构中
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

    print(cheap)
    print(expensive)
    # 上面代码在对每个元素进行对比的时候，会以 price 的值进行比较

    # 如果你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，
    # 那么这些函数提供了很好的性能。因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)

    # 剩余的元素可以很
    # 容易的通过调用 heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
    # 用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)，N 是
    # 堆大小）
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
