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
    #  This terminal is gate input
    IN = 0
    #  This terminal is gate output
    OUT = 1
    #  This terminal is wire input-output
    BOTH = 2


class Current(Enum):
    LOW = 0
    HIGH = 1


class Terminal:
    def __init__(self, direction, pin_set):
        if type(direction) is not Direction:
            raise TypeError('{} is not a Direction'.format(direction))
        if type(pin_set) is not PinSet:
            raise TypeError('{} is not a PinSet'.format(pin_set))

        self.__direction = direction
        self.__pin_set = pin_set
        self.__current = 0

    @property
    def direction(self):
        return self.__direction

    @property
    def pin_set(self):
        return self.__pin_set

    @property
    def current(self):
        return self.__current

    def reset(self):
        self.__current = Current.LOW

    def set_out(self, current):
        """
        sets the current on OUT pin.
        :param current:
        :return:
        """
        if type(current) is not Current:
            raise TypeError('{} is not a Current'.format(current))
        if self.pin_set == PinSet.OUT:
            self.__current = current
        else:
            raise OperationError('can\'t set pin current on {} terminal'.format(self.pin_set))

    def set_in(self, current):
        """
        sets the current on IN pin
        :param current:
        :return:
        """
        if type(current) is not Current:
            raise TypeError('{} is not a Current'.format(current))
        if self.pin_set == PinSet.IN:
            self.__current = current
        else:
            raise OperationError('can\'t set pin current on {} terminal'.format(self.pin_set))


class OccupationError(Exception):
    pass


class OperationError(Exception):
    pass

