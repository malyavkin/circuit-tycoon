import unittest

from helpers.helpers import is_tuple_of_n_ints


class HelpersTest(unittest.TestCase):
    def test_list_of_2_ints(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=[1, 2]))

    def test_tup_of_3_ints(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=(1, 2, 3)))

    def test_tup_of_floats(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=(1.1, 3)))

    def test_correct(self):
        self.assertTrue(is_tuple_of_n_ints(n=3, var=(1, 2, 3)))