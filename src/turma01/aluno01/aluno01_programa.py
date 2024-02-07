import pytest


'''        
def _validar(segundo, minuto, hora):
        return 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60
'''
def tique(hora, minuto, segundo):
        segundo += 1
        if segundo == 60:
            segundo = 0
            minuto += 1
            if minuto == 60:
                minuto = 0
                hora += 1
                if hora == 24:
                    hora = 0
        return hora, minuto, segundo



