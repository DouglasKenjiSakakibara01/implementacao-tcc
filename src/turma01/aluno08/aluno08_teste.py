#from aluno08_programa import tique

# Testes automatizados com pytest
#@pytest.fixture
def test_tique():
    assert tique(0,0,0) == (0,0,1)

def test_tique2():    
    assert tique(23, 59, 59) == (0, 0, 0)
