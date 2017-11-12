#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random


def qsort(l):
    if not l:
        return []
    else:
        x, xs = l[0], l[1:]
        lhs = [p for p in xs if p < x]
        rhs = [p for p in xs if p > x]
        return qsort(lhs) + [x] + qsort(rhs)


def main():
    inp_arr = [random.randint(0, 1000) for i in xrange(10)]
    out_arr = qsort(inp_arr)
    ref_arr = sorted(inp_arr)
    print "inp:", inp_arr
    print "out:", out_arr
    print "ref:", ref_arr


if __name__ == '__main__':
    main()
