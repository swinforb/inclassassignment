#############################
# Author: Ben Swinford
# Program: testLeap.py
# Date: 5/22/21
#############################

import unittest
import leapyear


class testLeapYear(unittest.TestCase):

	def test_negative_year(self):
		print("TEST NEGATIVE")
		results = leapyear.leapYears()
		userInput = results[0]
		self.assertLess(0, userInput)

	def test_is_int(self):
		print("TEST VALUE")
		with self.assertRaises(ValueError): leapyear.leapYears()

	def test_validity(self):
		print("TEST VALIDITY")
		results = leapyear.leapYears()
		expected = input("Do you expect the year to be a leap year? (y/n) : ")
		if expected == "y":
			expectede = 1
		else:
			expectede = 0
		self.assertTrue(results[1] == expectede)


if __name__ == '__main__':
	unittest.main()
