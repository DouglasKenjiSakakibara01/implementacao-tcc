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


# test_relogio_digital.py
#from aluno09_programa import tique
import pytest

# Testes para a operação Tique (Tick)

def test_tique():
    assert tique(12, 30 , 30) == (12, 30, 31)

def test_tique2():    
    assert tique(12, 30 , 59) == (12, 31, 0)

def test_tique3():    
    assert tique(12, 59 , 59) == (13, 0, 0)

def test_tique4():    
    assert tique(23, 59 , 59) == (0, 0, 0)

