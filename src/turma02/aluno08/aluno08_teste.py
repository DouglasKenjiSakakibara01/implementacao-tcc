def test_tique():
    assert tique(12, 30, 59) == (12, 31, 0)

def test_tique2():
    assert tique(23, 59, 59) == (0, 0, 0)
