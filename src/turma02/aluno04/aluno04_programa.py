def tique(hora, minuto, segundo):
        segundo = (segundo + 1) % 60
        if segundo == 0:
            minuto = (minuto + 1) % 60
            if minuto == 0:
                hora = (hora + 1) % 24

        return hora, minuto, segundo

