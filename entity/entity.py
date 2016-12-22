from helpers.helpers import is_tuple_of_n_ints


class Entity:

    def __init__(self, size):
        assert is_tuple_of_n_ints(n=2, var=size)
        self.size = size

    def get_occupation_profile(self, offset=(0, 0)):
        return {(i + offset[0], j + offset[1])
                for i in range(self.size[0])
                for j in range(self.size[1])}


