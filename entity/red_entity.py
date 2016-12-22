from entity.entity import Entity


class Conductor(Entity):
    """
    Conductor is a common class for all entities that can transmit electricity
    terminals define how can it be connected to anything else
    each terminal is:
        (i, j), DIRECTIONS.UP
    """
    def __init__(self, size, terminals):
        super().__init__(size)
        self.terminals = terminals


