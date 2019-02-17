#! /usr/bin/env python
#coding=utf-8

import unittest

def add(x,y):
    return x+y

class Demo(unittest.TestCase):

    def setUp(self):
        print("I am set up")

    def test_demo(self):
        print("my first unit test demo")
        self.assertEqual(add(10,9),11,"assert equal")

    def test_demo2(self):
        print("my first unit test demo")
        self.assertEqual(add(10,1),11,"assert equal in demo2")

    def tearDown(self):
        print("I am tear down")

