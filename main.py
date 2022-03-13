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


if __name__ == "__main__":
    parser = Parser()

    while parser.state == Parser.STATE_PARSING:
        parser.parse(input())

    if parser.state == Parser.STATE_ERROR:
        sys.exit("Illegal input.")

    ca = parser.create_ca()

    printGeneration(ca.cells)

    for _ in range(1, parser.generations):
        ca.next_generation()
        printGeneration(ca.cells)
