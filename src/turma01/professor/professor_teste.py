#from professor_programa import tique

def test_tique_seg():
    assert tique(12, 30, 45) == (12, 30, 46)

def test_tique_seg_limite():
    assert tique(23, 59, 59) == (0, 0, 0)

def test_tique_min():
    assert tique(10, 45, 59) == (10, 46, 0)

def test_tique_min_limite():
    assert tique(15, 59, 59) == (16, 0, 0)

def test_tique_hora():
    assert tique(22, 59, 30) == (22, 59, 31)

def test_tique_hora_limite():
    assert tique(23, 59, 59) == (0, 0, 0)

def test_tique_hora_min_limite():
    assert tique(23, 59, 58) == (23, 59, 59)

def test_tique_hora_min_seg_limite():
    assert tique(23, 59, 59) == (0, 0, 0)