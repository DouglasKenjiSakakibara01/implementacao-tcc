from aluno01_programa import verificaParidade

def test_paridade():
    assert verificaParidade(25)=='impar'
    assert verificaParidade(5)=='impar'
    assert verificaParidade(150)=='par'
    assert verificaParidade(1)=='impar'
    assert verificaParidade(10)=='par'
    assert verificaParidade(0)=='impar'
