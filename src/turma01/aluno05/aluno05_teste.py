from aluno05_programa import tique
# função tique() - casos de teste
def test_01():
	assert tique(18, 10, 30) == (18, 10, 31)

def test_02():
    assert tique(0, 0, 0) == (0, 0, 1)

def test_03():
    assert tique(23, 59, 59) == (0, 0, 0)