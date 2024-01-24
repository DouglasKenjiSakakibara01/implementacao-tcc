import pytest

#Calcula a média final de acordo com as 3 notas do aluno
def calcula_media(nota1, nota2, nota3):
    
    total = nota1 + nota2 + nota3
    mediaf = total / 3

    if mediaf >= 90:
        return 'A'
    elif mediaf >= 80:
        return 'B'
    elif mediaf >= 70:
        return 'C'
    elif mediaf >= 60:
        return 'D'
    else:
        return 'F'


def test_media():
    assert calcula_media(90,90,90) == 'A'  
    assert calcula_media(80,70,60) == 'C'
    assert calcula_media(60,60,60) == 'D'
