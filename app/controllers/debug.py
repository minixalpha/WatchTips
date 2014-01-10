#!/usr/bin/env python
#coding: utf-8

# Debug utils


def debug_bound(func):
    def wrapper(*args):
        print('*' * 16)
        result = func(*args)
        print('*' * 16)
        return result
    return wrapper


@debug_bound
def print_info(info):
    print(info)


@debug_bound
def print_iter_info(info):
    for key in info.items():
        print(key)
