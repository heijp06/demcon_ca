from functools import partial

class Parser:
    STATE_PARSING = 0
    STATE_FINAL = 1
    STATE_ERROR = 2

    def __init__(self) -> None:
        self.state = Parser.STATE_PARSING
        self._parse_func = self._read_type

    def parse(self, line: str) -> None:
        for field in line.split():
            if self.state != Parser.STATE_PARSING:
                self.state = Parser.STATE_ERROR
                return
            self._parse_func(field)

    def _read_type(self, field: str) -> None:
        if field not in "ABU":
            self.state = Parser.STATE_ERROR
            return
        self.type = field
        if field == "A":
            self.rule = 122
        elif field == "B":
            self.rule = 86
        else:
            self.rule = 0
        self._parse_func = self._read_length

    def _read_length(self, field: str) -> None:
        length = self._read_integer(field)
        if self.state == Parser.STATE_ERROR:
            return
        self.cells = [0] * length
        self._parse_func = self._read_generations

    def _read_generations(self, field: str) -> None:
        generations = self._read_integer(field)
        if self.state == Parser.STATE_ERROR:
            return
        self.generations = generations
        self._parse_func = self._read_init_start
    
    def _read_init_start(self, field: str) -> None:
        if field != "init_start":
            self.state = Parser.STATE_ERROR
            return
        self._parse_func = self._read_occupied
    
    def _read_occupied(self, field: str) -> None:
        if field == "init_end":
            if self.type in "AB":
                self.state = Parser.STATE_FINAL
            else:
                self._parse_func = partial(self._read_bit, 0)
            return
        occupied = self._read_integer(field)
        if self.state == Parser.STATE_ERROR:
            return
        if occupied < len(self.cells):
            self.cells[occupied - 1] = 1

    def _read_bit(self, bit: int, field: str) -> None:
        pass

    def _read_integer(self, field: str) -> int:
        try:
            result = int(field)
            if result < 1:
                self.state = Parser.STATE_ERROR
            return result
        except:
            self.state = Parser.STATE_ERROR
            return -1