from aluno10_programa import tique#@pytest.fixture

# Teste normal para a operação tique.
def test_tique():
    assert tique(0, 0, 0) == (0, 0, 0)

# Teste de tique que leva a meia-noite (overflow).
def test_tique_to_midnight(relogio):
    assert tique(0, 0, 0) == (0, 0, 0)

# Teste de tique imediatamente após meia-noite.
def test_tique_post_midnight(relogio):
    
    assert tique(23, 59, 58) == (23, 59, 59)
    
    assert tique(23, 59, 59)  == (0,0,0)

