from aluno04_programa import tique
"""Testes Tique"""

def test_tique_horario_valido():
    assert tique(8,25,54) == (8, 25,55)
    
'''
def test_tique_horario_invalido():
    horario = {'horas': 24, 'minutos': 59, 'segundos': 59}
    assert tique(horario) == "Horário inválido"
'''
def test_tique_horario_limite_superior():
    assert tique(23,59,59) == (0,0,0)

def test_tique_horario_limite_inferior():
    assert tique(0,0,0) == (0,0,1)

"""Fim Testes Tique"""
