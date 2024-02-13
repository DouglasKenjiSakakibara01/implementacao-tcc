def test_tique01():
    assert tique(12, 0, 0) == (12, 0, 1)
    

def test_tique02():
    assert tique(0, 0, 59) == (0, 1, 0)
   

def test_tique03():
    assert tique(0, 59, 59) == (1, 0, 0)

def test_tique04():
    assert tique(23, 59, 59) == (0, 0, 0)
    
