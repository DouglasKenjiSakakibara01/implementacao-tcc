"""
### Operação de tique
## Particionamentos:
    - Próximo a mudança de minuto (xx:yy:59) -> Valor limite
    - Próximo a mudança de hora (xx:59:59) -> Valor limite
    - Próximo a mudança de dia (23:59:59) -> Valor Limite
    - Mudança de horario padrão (Sem alterar minuto/hora/segundo)
"""
def test_tique_mudanca_segundos():
    # 00:00:59
    assert tique(0, 0, 59) == (00, 1, 00)

def test_tique_mudanca_minutos():
    # 00:59:59
    assert tique(0, 59, 0)== (1, 00, 00)

def test_tique_mudanca_horas():
    # 23:59:59
    assert tique(23, 59, 59) == (00, 00, 00)

def test_tique_mudanca_padrao():
    # 02:43:33
    assert tique(2, 43, 33) == (2, 43, 34)

