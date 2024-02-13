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


from aluno08_programa import tique

# Testes automatizados com pytest
#@pytest.fixture
def test_tique():
    assert tique(0,0,0) == (0,0,1)

def test_tique2():    
    assert tique(23, 59, 59) == (0, 0, 0)
