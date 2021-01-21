#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:20:55 2021

@author: silasjimmy
"""

def count_words(s, n):
    s = s.split(' ')
    counted_words = [(w, s.count((w))) for w in set(s)]
    counted_words.sort(key = lambda x: (-x[1], x[0]))
    top_n = counted_words[:n]
    return top_n

def test_run():
    print(count_words('cat bat mat cat bat cat', 3))
    print(count_words('betty bought a bit of butter but the butter was bitter', 3))
    
if __name__ == '__main__':
    test_run()
