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


#from aluno12_programa import tique
def test_modifica_s():
  
    assert tique(20, 30, 5) == (20, 30, 6)

def test_modifica_sm():
 
    assert tique(0, 15, 59) == (0,16,0)

def test_modifica_smh():

    assert tique(8, 59, 59)== (9,0,0)

def test_reset_clock():
    
    assert tique(23, 59, 59) == (0,0,0)

