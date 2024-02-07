from aluno12_programa import tique
def test_modifica_s():
  
    assert tique(20, 30, 5) == (20, 30, 5)

def test_modifica_sm():
 
    assert tique(0, 15, 59) == (0,16,0)

def test_modifica_smh():

    assert tique(8, 59, 59)== (9,0,0)

def test_reset_clock():
    
    assert tique(23, 59, 59) == (0,0,0)

