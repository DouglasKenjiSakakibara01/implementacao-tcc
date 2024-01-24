IDADE_LEGAL = 18
SUGESTAO = 'copo d\'água'

def verifica_bebida(idade, bebida, alcool, sugestao=SUGESTAO):
    if idade < IDADE_LEGAL and alcool:
        return False, sugestao
    else:
        return True, bebida
def test_maior_pede_cerveja():
        assert verifica_bebida(30, 'cerveja', True) == (True,
                                                        'cerveja')
def test_menor_pede_suco():
        assert verifica_bebida(15, 'suco', False) == (True,
                                                      'suco')   

    

 