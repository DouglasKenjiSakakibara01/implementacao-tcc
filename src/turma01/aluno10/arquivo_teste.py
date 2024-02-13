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


#from aluno10_programa import tique
#@pytest.fixture

# Teste normal para a operação tique.
def test_tique():
    assert tique(0, 0, 0) == (0, 0, 0)

# Teste de tique que leva a meia-noite (overflow).
def test_tique_to_midnight():
    assert tique(0, 0, 0) == (0, 0, 0)

# Teste de tique imediatamente após meia-noite.
def test_tique_post_midnight():
    
    assert tique(23, 59, 58) == (23, 59, 59)
    
    assert tique(23, 59, 59)  == (0,0,0)

