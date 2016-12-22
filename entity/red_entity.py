from entity.entity import Entity
from helpers.helpers import Terminal, Direction, PinSet


class Conductor(Entity):
    """
    Conductor is a common class for all entities that can transmit electricity
    terminals define how can it be connected to anything else
    each terminal is:
        (i, j), DIRECTIONS.UP
    """
    def __init__(self, size, terminals):
        super().__init__(size)
        for terminal in terminals:
            assert type(terminal) is Terminal


class StraightWire(Conductor):
    def __init__(self):
        super().__init__((1, 1), [
            Terminal((0, 0), Direction.DOWN, PinSet.BOTH),
            Terminal((0, 0), Direction.UP, PinSet.BOTH),
        ])
