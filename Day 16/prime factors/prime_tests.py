import unittest

from prime_factors import (
	factors,
)

class Unittesting(unittest.TestCase):
	# def no_factors(self):
	# 	self.assertEqual(factors(1), [])
	
	# def test_prime_number(self):
	# 	self.assertEqual(factors(2), [2])
	
	def test_another_prime_number(self):
		self.assertEqual(factors(3), [3])

	def random_number(self):
		self.assertEqual(factors(115), [3])

unittest.main()
