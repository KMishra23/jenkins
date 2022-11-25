#!/usr/bin/python3

import unittest
from armstrong import isArmstrong

class Testcases(unittest.TestCase):
	def testcase1(self):
		self.assertEqual(isArmstrong(1),False)

	def testcase2(self):
		self.assertEqual(isArmstrong(407),False)

	def testcase3(self):
		self.assertEqual(isArmstrong(567),True)

if __name__ == '__main__':
	unittest.main()