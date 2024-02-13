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

