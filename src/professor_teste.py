from professor_programa import verificaParidade

def test_par():
    assert verificaParidade(150)=='par'
    assert verificaParidade(10)=='par'
    assert verificaParidade(20)=='par'



def test_impar():
    assert verificaParidade(25)=='impar'
    assert verificaParidade(8)=='impar'
    assert verificaParidade(1)=='impar'
    assert verificaParidade(0)=='impar'

def test_outro():
    assert verificaParidade(1)=='impar'
    assert verificaParidade(90)=='impar'
    