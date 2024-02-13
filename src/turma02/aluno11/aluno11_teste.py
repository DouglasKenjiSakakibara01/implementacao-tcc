import pytest

def test_tique_valido():
    assert tique(23, 59, 59) == (00, 00, 00)
    assert tique(00, 00, 00) == (00, 00, 1)

# HORAS
def test_tique_hora_imediatamente_abaixo():
    assert tique(-1, 10, 34) == (-1, -1, -1)
    assert tique(22, 10, 34) == (22, 10, 35)

def test_tique_hora_exato_do_limite():
    assert tique(00, 10, 34) == (00, 10, 35)
    assert tique(23, 10, 34) == (23, 10, 35)

def test_tique_hora_imediatamente_acima():
    assert tique(1, 10, 34) == (1, 10, 35)
    assert tique(24, 10, 34) == (-1, -1, -1)

# MINUTOS
def test_tique_minuto_imediatamente_abaixo():
    assert tique(15, 1, 51) == (-1, -1, -1)
    assert tique(15, 58, 51) == (15, 58, 52)

def test_tique_minuto_exato_do_limite():
    assert tique(15, 0, 51) == (15, 00, 52)
    assert tique(15, 59,51) == (15, 59, 52)

def test_tique_minuto_imediatamente_acima():
    assert tique(15, 1, 51) == (15, 1, 52)
    assert tique(15, 60, 51) == (-1, -1, -1)

#SEGUNDOS
def test_tique_segundo_imediatamente_abaixo():
    assert tique(17, 43, -1) == (-1, -1, -1)
    assert tique(17, 43, 58) == (17, 43, 59)

def test_tique_segundo_exato_do_limite():
    assert tique(17, 43, 00) == (17, 43, 1)
    assert tique(17, 43, 59) == (17, 44, 00)

def test_tique_segundo_imediatamente_acima():
    assert tique(17, 43, 1) == (17, 43, 2)
    assert tique(17, 43, 60) == (-1, -1, -1)
