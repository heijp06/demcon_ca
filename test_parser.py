from parser import Parser


def test_parse_a():
    parser = Parser()
    parser.parse("A 11 10")
    parser.parse("init_start 6 init_end")

    expected_cells = [False] * 11
    expected_cells[5] = True

    assert parser.state == Parser.STATE_FINAL
    assert parser.type == "A"
    assert parser.cells == expected_cells
    assert parser.generations == 10
    assert parser.rule == 122


def test_parse_b():
    parser = Parser()
    parser.parse("B 61 20")
    parser.parse("init_start 20 40 init_end")

    expected_cells = [False] * 61
    expected_cells[19] = True
    expected_cells[39] = True

    assert parser.state == Parser.STATE_FINAL
    assert parser.type == "B"
    assert parser.cells == expected_cells
    assert parser.generations == 20
    assert parser.rule == 86


def test_parse_u_129():
    parser = Parser()
    parser.parse("U 61 20")
    parser.parse("init_start 30 init_end")
    parser.parse("1 0 0 0 0 0 0 1")

    expected_cells = [False] * 61
    expected_cells[29] = True

    assert parser.state == Parser.STATE_FINAL
    assert parser.type == "U"
    assert parser.cells == expected_cells
    assert parser.generations == 20
    assert parser.rule == 129
