class CA:
    def __init__(self, cells: list[bool], rule: int) -> None:
        self.cells = cells
        self.rule = rule
        self.left_edge = False
        self.right_edge = False

    def next_generation(self) -> None:
        extended = [self.left_edge] + self.cells + [self.right_edge]
        self.cells = [
            self.next_cell(previous)
            for previous
            in zip(extended, extended[1:], extended[2:])
        ]
        self.left_edge = self.next_cell(tuple([self.left_edge] * 3))
        self.right_edge = self.next_cell(tuple([self.right_edge] * 3))

    def next_cell(self, previous: tuple[bool, ...]) -> bool:
        left, cell, right = previous
        return self.rule & (1 << left * 4 + cell * 2 + right) != 0
