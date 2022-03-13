class CA:
    def __init__(self, cells: list[bool], rule: int) -> None:
        self.cells = cells
        self.rule = rule
        self.value_at_infinity = False

    def next_generation(self) -> None:
        extended = [
            self.value_at_infinity, *self.cells, self.value_at_infinity
        ]
        self.cells = [
            self.next_cell(left, cell, right)
            for left, cell, right
            in zip(extended, extended[1:], extended[2:])
        ]
        self.value_at_infinity = self.next_cell(
            self.value_at_infinity, self.value_at_infinity, self.value_at_infinity
        )

    def next_cell(self, left: bool, cell: bool, right: bool) -> bool:
        return self.rule & (1 << left * 4 + cell * 2 + right) != 0
