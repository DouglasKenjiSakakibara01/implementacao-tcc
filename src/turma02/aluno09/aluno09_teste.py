def test_tique():
    # Classe de equivalência 1: Horários que não causam transbordamento
    assert tique(12, 59, 31) == (12, 59, 32)

def test_tique2():
    # Classe de Equivalência 2: Horários que causam transbordamento nos segundos
    assert tique(12, 58, 59) == (12, 59, 0)

def test_tique3():
    # Classe de Equivalência 3: Horários que causam transbordamento nos minutos
    assert tique(11, 59, 30) == (12, 0, 30)

 
def teste_tique4():
    # Classe de Equivalência 4: Horários que causam transbordamento nas horas
    assert tique(23, 59, 59) == (0, 0, 0)




