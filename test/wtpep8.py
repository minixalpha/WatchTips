#!/usr/bin/env python
#coding: utf-8

# PEP8 test case


import watchtipstest
import fnmatch
import os
import unittest


class TestPEP8(unittest.TestCase):
    def get_all_files(self, dir, ext):
        match_files = []
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, ext):
                match_files.append(os.path.join(root, filename))

        return match_files

    def test_pep8(self):
        cur_dir = os.path.curdir
        py_files = self.get_all_files(cur_dir, '*.py')
        cmd_teplate = 'pep8 {file_path}'
        succeed = 0
        result = succeed
        for py_file in py_files:
            cmd = cmd_teplate.format(file_path=py_file)
            result = os.system(cmd)
            if not succeed == result:
                break
        self.assertEqual(result, succeed)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPEP8)
    watchtipstest.main(suite)
