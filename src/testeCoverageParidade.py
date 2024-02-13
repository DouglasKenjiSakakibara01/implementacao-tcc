import pytest

# Verifica a paridade do numero inteiro
def verificaParidade(num):

    if type(num) == int :
        if num % 2 == 0 or num==0:
            return 'par'
        else:
            return 'impar'
    else: # Caso o numero nao seja inteiro nao e possivel verificar a paridade
        print('Numero nao inteiro')
        return 'erro'
'''
def test_paridade():
    assert verificaParidade(25)=='impar'
    assert verificaParidade(5)=='impar'
    assert verificaParidade(150)=='par'
    assert verificaParidade(1)=='impar'
    assert verificaParidade(10)=='par'
    assert verificaParidade(0)=='impar'

'''
    