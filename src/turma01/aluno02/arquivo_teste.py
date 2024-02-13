def tique(horas, minutos, segundos):
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
            if horas == 24:
                horas = 0
    return horas, minutos, segundos


#from aluno02_programa import tique

# Testes para o método tique
def test_01():
    assert tique(12, 30, 45) == (12, 30, 46)
    
def test_02():
    assert tique(0, 0, 0) == (0, 0, 1)
   

def test_03():
    assert tique(23, 59, 59) == (0, 0, 0)
   
