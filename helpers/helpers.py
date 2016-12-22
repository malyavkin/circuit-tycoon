from enum import Enum


def is_tuple_of_n_ints(n, var):
    if type(var) is not tuple:
        return False
    if len(var) != n:
        return False
    for i in var:
        if type(i) is not int:
            return False
    return True


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class PinSet(Enum):
    IN = 0
    OUT = 1
    BOTH = 2


class Terminal:
    def __init__(self, position, direction, pin_set):
        if type(direction) is not Direction:
            raise TypeError('{} is not a Direction'.format(direction))
        if type(pin_set) is not PinSet:
            raise TypeError('{} is not a PinSet'.format(pin_set))
        if not is_tuple_of_n_ints(var=position, n=2):
            raise ValueError('{} should be tuple(int, int)'.format(position))

        self.position = position
        self.direction = direction
        self.pin_set = pin_set
