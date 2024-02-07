from aluno06_programa import tique

def test_tique():
    assert tique(0, 0, 0) == (0,0,1)

def test_tique2():
    assert tique(14,40,58 ) == (14, 40,59)
    
def test_tique3():
    assert tique(14,40,59) == (14,42,0)

def test_tique4():
    assert tique(14,59,59) == (15,0,0)
    
def test_tique5():
    assert tique(23,59,59) == (0,0,0)
    

