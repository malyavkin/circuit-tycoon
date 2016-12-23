from entity.entity import Entity
from helpers.helpers import Terminal, Direction, PinSet, OperationError, is_tuple_of_n_ints, Current


class Conductor(Entity):
    """
    Conductor is a common class for all entities that can transmit electricity
    terminals define how can it be connected to anything else
    each terminal is:
        (i, j), DIRECTIONS.UP
    """
    def __init__(self, size, terminals):
        super().__init__(size)
        for position, terminal in terminals:
            assert type(terminal) is Terminal
            assert is_tuple_of_n_ints(n=2, var=position)
        self.terminals = terminals

    def reset(self):
        for terminal in self.terminals:
            terminal.reset()


class StraightWire(Conductor):
    def __init__(self):
        super().__init__((1, 1), [
            ((0, 0), Terminal(Direction.DOWN, PinSet.BOTH)),
            ((0, 0), Terminal(Direction.UP, PinSet.BOTH)),
        ])


class Gate(Conductor):
    def __init__(self, size, terminals):
        super().__init__(size, terminals)
        self.state = {}

    def step(self):
        raise OperationError('Gate is an abstract class, you can\'t use it directly')


class PowerSupply(Gate):
    def __init__(self):
        super().__init__((1, 1), [
            ((0, 0), Terminal(Direction.DOWN, PinSet.OUT)),
            ((0, 0), Terminal(Direction.UP, PinSet.OUT)),
            ((0, 0), Terminal(Direction.LEFT, PinSet.OUT)),
            ((0, 0), Terminal(Direction.RIGHT, PinSet.OUT)),
        ])

    def step(self):
        for position, terminal in self.terminals:
            terminal.set_out(Current.HIGH)


class Lamp(Gate):
    def __init__(self):
        super().__init__((1, 1), [
            ((0, 0), Terminal(Direction.DOWN, PinSet.IN)),
            ((0, 0), Terminal(Direction.UP, PinSet.IN)),
            ((0, 0), Terminal(Direction.LEFT, PinSet.IN)),
            ((0, 0), Terminal(Direction.RIGHT, PinSet.IN)),
        ])
        self.state = {
            'power': Current.LOW
        }

    def step(self):
        for position, terminal in self.terminals:
            if terminal.current == Current.HIGH:
                self.state['power'] = Current.HIGH
