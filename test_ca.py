from cellular_automaton import CA

def test_next_generation():
    ca = CA([False, True, False], 122)
    ca.next_generation()
    
    assert ca.cells == [True, False, True]

def test_next_generation_edge():
    ca = CA([False, False, False, False, True, False, False, False, False], 129)
    gen2 = [True, True, True, False, False, False, True, True, True]
    gen3 = [True, True, False, False, True, False, False, True, True]

    ca.next_generation()
    assert ca.cells == gen2

    ca.next_generation()
    assert ca.cells == gen3