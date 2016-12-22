from entity.entity import Entity
from helpers.helpers import is_tuple_of_n_ints


class OccupationError(Exception):
    pass


class Field:
    def __init__(self):
        self.contents = []

    def insert(self, entity, position):
        """
        inserts entity at position
        :param entity:
        :param position:
        :return:
        """
        if type(entity) is not Entity:
            raise TypeError('{} is not an Entity'.format(entity))
        if not is_tuple_of_n_ints(var=position, n=2):
            raise ValueError('{} should be tuple(int, int)'.format(position))
        if self.can_be_placed(entity, position):
            self.contents.append((
                position,
                entity
            ))
        else:
            raise OccupationError()

    def can_be_placed(self, entity, position):
        all_free = True
        for pos in entity.get_occupation_profile(position):
            if self.query(pos):
                all_free = False
        return all_free

    def query(self, asked):
        """
        checks if given position is occupied
        :param asked:
        :return:
        """
        assert is_tuple_of_n_ints(var=asked, n=2)
        entities = [
            entity
            for position, entity in self.contents
            if (position[0] <= asked[0] and
                position[1] <= asked[1] and
                position[0] + entity.size[0] > asked[0] and
                position[1] + entity.size[1] > asked[1])
        ]
        return entities
