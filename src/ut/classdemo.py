#!/usr/bin/env python
# encoding: utf-8


import unittest


class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("setup method")
        simple_test.foo = list(range(10))
        print(str(simple_test.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(simple_test.foo.pop(), 9)

    def test_2nd(self):
        print('test_2nd')
        print("test_2nd:"+str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 9)

    @classmethod
    def tearDownClass(cls):
        print("end method")


if __name__ == '__main__':
    unittest.main()
