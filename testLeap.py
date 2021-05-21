#############################
# Author: Ben Swinford
# Program: testLeap.py
# Date: 5/22/21
#############################

import unittest


class testLeapYear(unittest.TestCase):

	def test_negative_year(self):
		results = leapyear.leapYear()
		userInput = results[0]
		self.assertLessThan(0, userInput)

	def test_is_int(self):
		with self.assertRaises(TypeError): leapyear.leapYear()

	def test_validity(self):
		results = leap.leapYear()
		expected = input("Do you expect the year to be a leap year? (y/n) : ")
		if expected == "y":
			expectede = 1
		else:
			expectede = 0
		self.assertTrue(results[1] == expectede)
