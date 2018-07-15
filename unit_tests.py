#!/usr/bin/env python3
# Test cases for bowling scoring program
# Author: Kaushal Thaker

import unittest
from score import *

class BowlingTests(unittest.TestCase):

	def test_strikes(self):
		rolls = convert("XXXXXXXXXXXX")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 300)

	def test_nines(self):
		rolls = convert("9-9-9-9-9-9-9-9-9-9-")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 90)

	def test_spares(self):
		rolls = convert("5/5/5/5/5/5/5/5/5/5/5")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 150)

	def test_typical(self):
		rolls = convert("X7/9-X-88/-6XXX81")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 167)

	def test_one(self):
		rolls = convert("X--X--X--X--X--")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 50)

	def test_two(self):
		rolls = convert("-/-/-/-/-/-/-/-/-/-/-")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 100)

	def test_three(self):
		rolls = convert("--------------------")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 0)

	def test_four(self):
		rolls = convert("5-X-91/-/537/X8-XXX")
		total_score = score(rolls, 0, 1)
		self.assertEqual(total_score, 142)

if __name__ == "__main__":
    unittest.main()