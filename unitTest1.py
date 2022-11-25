#!/usr/bin/python3

import unittest
from armstrong import isArmstrong

class Testcases(unittest.TestCase):
	def testcase1(self):
		self.assertEqual(isArmstrong(153),True)

	def testcase3(self):
		self.assertEqual(isArmstrong(1634),True)

	def testcase2(self):
		self.assertEqual(isArmstrong(1589),False)

	def testcase4(self):
		self.assertEqual(isArmstrong(35),False)

if __name__ == '__main__':
	unittest.main()