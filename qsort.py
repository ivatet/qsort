#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random


def partial_impl(arr, low, high):
    pi = arr[high]
    i = low
    for j in xrange(low, high):
        if (arr[j] < pi):
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def qsort_impl(arr, low, high):
    if (low < high):
        pi = partial_impl(arr, low, high)
        qsort_impl(arr, low, pi - 1)
        qsort_impl(arr, pi + 1, high)


def qsort(arr):
    copied_arr = copy.copy(arr)
    qsort_impl(copied_arr, 0, len(copied_arr) - 1)
    return copied_arr


def main():
    inp_arr = [random.randint(0, 1000) for i in xrange(10)]
    out_arr = qsort(inp_arr)
    ref_arr = sorted(inp_arr)
    print "inp:", inp_arr
    print "out:", out_arr
    print "ref:", ref_arr


if __name__ == '__main__':
    main()
