import unittest

from helpers.helpers import is_tuple_of_n_ints, Terminal, Direction, PinSet, Current, OperationError


class HelpersTest(unittest.TestCase):
    def test_list_of_2_ints(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=[1, 2]))

    def test_tup_of_3_ints(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=(1, 2, 3)))

    def test_tup_of_floats(self):
        self.assertFalse(is_tuple_of_n_ints(n=2, var=(1.1, 3)))

    def test_correct(self):
        self.assertTrue(is_tuple_of_n_ints(n=3, var=(1, 2, 3)))


class TerminalTests(unittest.TestCase):
    def test_regular_terminal(self):
        t = Terminal(Direction.UP, PinSet.OUT)
        t.set_out(Current.HIGH)
        self.assertEqual(t.current, Current.HIGH)

    def test_regular_terminal_wrong_direction(self):
        with self.assertRaises(TypeError):
            t = Terminal(0, PinSet.OUT)

    def test_regular_terminal_wrong_pin_set(self):
        with self.assertRaises(TypeError):
            t = Terminal(Direction.DOWN, 0)

    def test_regular_terminal_wrong_current(self):
        with self.assertRaises(TypeError):
            t = Terminal(Direction.DOWN, PinSet.OUT)
            t.set_out(0)

    def test_regular_terminal_set_current_on_IN(self):
        with self.assertRaises(OperationError):
            t = Terminal(Direction.DOWN, PinSet.IN)
            t.set_out(Current.HIGH)