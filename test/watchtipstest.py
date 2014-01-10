#!/usr/bin/env python
#coding: utf-8

# Test Entry Point

import sys
import unittest

# add top dir to module search path
sys.path.insert(0, '.')


def main(suite=None):
    if not suite:
        unittest.main()
    else:
        unittest.TestSuite(suite)
        runner = unittest.TextTestRunner()
        runner.run(suite)
