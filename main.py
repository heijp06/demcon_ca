import sys
from parser import Parser


def printGeneration(aGeneration):
    myprintString = ""
    for i in aGeneration:
        if i == True:
            myprintString += "*"
        else:
            myprintString += " "
    print(myprintString)


def next_generation(cells: list[bool], rule: int) -> list[bool]:
    extended = [0] + cells + [0]
    return [
        rule & (1 << left * 4 + cell * 2 + right) != 0
        for left, cell, right
        in zip(extended, extended[1:], extended[2:])
    ]


if __name__ == "__main__":
    parser = Parser()

    while parser.state == Parser.STATE_PARSING:
        parser.parse(input())

    if parser.state == Parser.STATE_ERROR:
        sys.exit("Illegal input.")

    cells = parser.cells
    printGeneration(cells)

    for _ in range(1, parser.generations):
        cells = next_generation(cells, parser.rule)
        printGeneration(cells)
