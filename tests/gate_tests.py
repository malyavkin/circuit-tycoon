import unittest

from entity.red_entity import PowerSupply
from helpers.helpers import Current


class GateTests(unittest.TestCase):
    def test_power_source(self):
        pc = PowerSupply()
        pc.step()
        for pos, term in pc.terminals:
            self.assertEqual(term.current, Current.HIGH)