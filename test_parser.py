from parser import Parser


def test_parse_a():
    parser = Parser()
    parser.parse("A 11 10")
    parser.parse("init_start 6 init_end")

    expected_cells = [0] * 11
    expected_cells[5] = 1

    assert parser.state == Parser.STATE_FINAL
    assert parser.type == "A"
    assert parser.cells == expected_cells
    assert parser.generations == 10
    assert parser.rule == 122


def test_parse_b():
    parser = Parser()
    parser.parse("B 61 20")
    parser.parse("init_start 20 40 init_end")

    expected_cells = [0] * 61
    expected_cells[19] = 1
    expected_cells[39] = 1

    assert parser.state == Parser.STATE_FINAL
    assert parser.type == "B"
    assert parser.cells == expected_cells
    assert parser.generations == 20
    assert parser.rule == 86
