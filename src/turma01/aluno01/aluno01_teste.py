from aluno01_programa import tique

def test_tique01():
    assert tique(12, 30, 45)== (12, 30, 46)

def test_tique02():   
    assert tique(23, 59, 59) == (0, 0, 0)
    
def test_tique03():    
    assert tique(23, 59, 59) == (0, 0, 1)