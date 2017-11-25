#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import copy
import random


def qsort(l):
    if not l:
        return []
    else:
        x, xs = l[0], l[1:]
        lhs = [p for p in xs if p < x]
        rhs = [p for p in xs if p >= x]
        return qsort(lhs) + [x] + qsort(rhs)


def main():
    inp = [random.randint(0, 1000) for i in xrange(10)]
    out = qsort(inp)
    ref = sorted(inp)
    print "inp:", inp
    print "out:", out
    print "ref:", ref
    sys.exit(out != ref)


if __name__ == '__main__':
    main()
