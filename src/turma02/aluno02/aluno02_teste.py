def test_tick():
    assert tique(0, 0, 0) == (00, 00, 1)

def test_tick_multiple_times():
    assert tique(0, 0,0) == (0, 0 ,1)
    assert tique(0, 0,1) == (0, 0 ,2)
    assert tique(0, 0,2) == (0, 0 ,3)

def test_tick_wraps_around_to_zero():
    assert tique(23, 59, 59) == (00, 00, 00)
