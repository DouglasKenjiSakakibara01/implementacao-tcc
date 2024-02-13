#from aluno03_programa import tique

def test_tique():
    assert tique(0, 0, 59) == (0, 1, 0)
    
def test_tique2():    
    assert tique(0, 59, 59) == (1, 0, 0)
    
def test_tique3():  
    assert tique(23, 59, 59) == (0, 0, 0)
   
def test_tique4():
    assert tique(0, 30, 0) == (0, 30, 1)
 

