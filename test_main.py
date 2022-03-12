from main import next_generation

def test_next_generation():
    assert next_generation([False, True, False], 122) == [True, False, True]
    