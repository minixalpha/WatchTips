#!/usr/bin/env python
#coding: utf-8

# Test on app.controllers.auth

import random
import string
import unittest

import watchtipstest
import app.controllers.auth as auth


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.test_times = 100

    def randomString(self):
        input_char = (
                string.ascii_letters +
                string.digits +
                string.punctuation)
        random_len = random.randint(1, 20)
        random_str = []
        for i in range(random_len):
            random_str.append(random.choice(input_char))
        return ''.join(random_str)

    def testEncrypPassword(self):
        for i in range(self.test_times):
            random_pwd = self.randomString()
            hashed_pwd = auth.encrypt_password(random_pwd)
            is_valid = auth.validate_password(hashed_pwd, random_pwd)
            assert is_valid, 'Error'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
    watchtipstest.main(suite)
