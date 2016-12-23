import unittest

from entity.entity import Entity
from field import Field
from helpers.helpers import OccupationError


def setup_field():
    field = Field()
    entity = Entity((1, 2))

    #   |-|-| |+|+|+|
    #   |2|1|0|1|2|3|
    # --+-+-+-+-+-+-+
    # -1| | | | | | |
    # --+-+-+-+-+-+-+
    #  0| | |#|#| | |
    # --+-+-+-+-+-+-+
    # +1| | | | | | |
    # --+-+-+-+-+-+-+

    field.contents = [
        ((0, 0), entity)
    ]
    return field, entity


class FieldTests(unittest.TestCase):
    def test_query_for_empty_field(self):
        field = Field()
        results = field.query((0, 0))
        self.assertFalse(results)

    def test_query_for_entity(self):
        field, entity = setup_field()
        results = field.query((0, 0))
        self.assertTrue(results)
        self.assertEqual(results[0], entity)

        results = field.query((0, 1))
        self.assertTrue(results)
        self.assertEqual(results[0], entity)

    def test_query_for_too_right(self):
        field, entity = setup_field()
        results = field.query((0, 2))
        self.assertFalse(results)

    def test_query_for_too_left(self):
        field, entity = setup_field()
        results = field.query((0, -1))
        self.assertFalse(results)

    def test_query_for_too_down(self):
        field, entity = setup_field()
        results = field.query((1, 0))
        self.assertFalse(results)

    def test_query_for_too_down_2(self):
        field, entity = setup_field()
        results = field.query((2, 0))
        self.assertFalse(results)

    def test_query_for_too_up(self):
        field, entity = setup_field()
        results = field.query((-1, 0))
        self.assertFalse(results)

    def test_query_for_too_down_3(self):
        field, entity = setup_field()
        results = field.query((1, 1))
        self.assertFalse(results)

    def test_query_for_too_up_2(self):
        field, entity = setup_field()
        results = field.query((-1, 1))
        self.assertFalse(results)

    def test_insert_not_entity(self):
        field = Field()
        with self.assertRaises(TypeError):
            field.insert('hello', (0, 0))

    def test_insert_wrong_position(self):
        field = Field()
        with self.assertRaises(ValueError):
            field.insert(Entity((1, 2)), (0, 0, 0))


class EntityTests(unittest.TestCase):
    def test_occupation_profile(self):
        entity = Entity((1, 2))
        profile = entity.get_occupation_profile((1, 2))
        self.assertSetEqual(profile,
                            {(1, 2), (1, 3)})


class InsertTests(unittest.TestCase):
    def test_insert_empty_field(self):
        field = Field()
        entity = Entity((1, 2))
        field.insert(entity, (1, 1))
        self.assertEqual(len(field.contents), 1)

    def test_occupation_check_fail(self):
        field = Field()
        en1 = Entity((1, 2))
        en2 = Entity((1, 2))
        field.insert(en1, (0, 0))
        with self.assertRaises(OccupationError):
            field.insert(en2, (0, 1))

    def test_occupation_check_success(self):
        field = Field()
        en1 = Entity((1, 2))
        en2 = Entity((1, 2))
        field.insert(en1, (0, 0))
        field.insert(en2, (0, 2))
        self.assertEqual(len(field.contents), 2)
