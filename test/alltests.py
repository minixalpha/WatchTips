#!/usr/bin/env python
#coding: utf-8

# Test all test case

import watchtipstest
import importlib
import unittest

g_module_names = ['appcontrollers', 'auth', 'wtpep8']


def get_suite_from_module_names(module_names):
    suite = unittest.TestSuite()
    for module_name in module_names:
        module = importlib.import_module(module_name)
        module_suite = unittest.TestLoader().loadTestsFromModule(module)
        suite.addTest(module_suite)
    return suite

if __name__ == '__main__':
    suite = get_suite_from_module_names(g_module_names)
    watchtipstest.main(suite)
