#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gaochen on 2022/8/4
# 1.12 序列中出现次数最多的元素.py
# 怎样找出一个序列中出现次数最多的元素呢？

if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter

    word_counts = Counter(words)
    # 出现频率最高的 3 个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]
