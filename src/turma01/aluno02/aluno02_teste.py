#from aluno02_programa import tique

# Testes para o método tique
def test_01():
    assert tique(12, 30, 45) == (12, 30, 46)
    
def test_02():
    assert tique(0, 0, 0) == (0, 0, 1)
   

def test_03():
    assert tique(23, 59, 59) == (0, 0, 0)
   
