#!/usr/bin/env python
#coding: utf-8

import watchtipstest
import unittest
from index import app


class AppController(unittest.TestCase):
    def testPageView(self):
        url_ok = ['/', '/watch/2', '/register', '/login']
        method = 'GET'
        status_ok = '200 OK'

        for url in url_ok:
            response = app.request(url, method=method)
            self.assertEqual(response.status, status_ok)

    def testNotFound(self):
        url = '/8'
        method = 'GET'
        status = '404 Not Found'
        response = app.request(url, method=method)
        self.assertEqual(response.status, status)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppController)
    watchtipstest.main(suite)
