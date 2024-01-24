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