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


#from aluno11_programa import tique


def test_tique():
    assert tique(12, 31, 43) == (12, 31, 44)
    assert tique(22, 55, 58) == (22, 55, 59)

def test_tique2():
    assert tique(2, 41, 59) == (2, 42, 0)
    assert tique(15, 19, 59) == (15, 20, 0)

def test_tique3():
    assert tique(0, 59, 59) == (1, 0, 0)
    assert tique(15, 59, 59) == (16, 0, 0)
    
def test_tique4():
    assert tique(23, 59, 59) == (0, 0, 0)

   