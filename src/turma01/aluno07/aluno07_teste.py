#from aluno07_programa import tique

# Casos de teste:

def teste_tique1():
    assert tique(12, 35, 42) == (12, 35, 43)
    
def teste_tique2():
    assert tique(23,59,59) == (0,0,0)
   
def teste_tique3():
    assert tique(0,0,0) == (0,0,1)
